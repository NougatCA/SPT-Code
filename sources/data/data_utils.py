import re
import tokenize
from io import StringIO
import json
import os
import logging
from tqdm import tqdm
from antlr4 import InputStream
import nltk

from .asts.ast_parser import generate_single_ast_nl, split_identifier
import enums
from data.vocab import Vocab
from data.antlr_parsers.go.GoLexer import GoLexer
from data.antlr_parsers.java.Java8Lexer import Java8Lexer
from data.antlr_parsers.python3.Python3Lexer import Python3Lexer
from data.antlr_parsers.php.PhpLexer import PhpLexer
from data.antlr_parsers.javascript.JavaScriptLexer import JavaScriptLexer
from data.code_tokenizers.ruby.ruby_tokenizer import RubyTokenizer

logger = logging.getLogger(__name__)

STRING_MATCHING_PATTERN = re.compile(r'([bruf]*)(\"\"\"|\'\'\'|\"|\')(?:(?!\2)(?:\\.|[^\\]))*\2')
NON_SPACE_MATCHING_PATTERN = re.compile(r'\S')

MAPPING_LANG_LEXER = {
    enums.LANG_GO: GoLexer,
    enums.LANG_JAVA: Java8Lexer,
    enums.LANG_PYTHON: Python3Lexer,
    enums.LANG_PHP: PhpLexer,
    enums.LANG_JAVASCRIPT: JavaScriptLexer,
    enums.LANG_RUBY: RubyTokenizer()
}


def load_eval_lines(path):
    """
    Load and eval lines from given path.

    Args:
        path (str): Dataset file path

    Returns:
        list: List of lines

    """
    with open(path, encoding='utf-8') as f:
        lines = [eval(line.strip()) for line in f]
    return lines


def load_eval_list_lines(path):
    """
    Load and eval lines from given path, each line is a list that will be convert into a string.

    Args:
        path (str): Dataset file path

    Returns:
        list: List of lines

    """
    lines = []
    with open(path, encoding='utf-8') as f:
        for line in f.readlines():
            tokens = eval(line.strip())
            string = ' '.join(tokens)
            string = re.sub(r'\s+', ' ', string)
            lines.append(string)
    return lines


def load_lines(path):
    """
    Load lines from given path.

    Args:
        path (str): Dataset file path

    Returns:
        list: List of lines

    """
    with open(path, encoding='utf-8') as f:
        lines = [line.strip() for line in f]
    return lines


def trim_method_name(full_name):
    """
    Extract method/function name from its full name,
    e.g., RpcResponseResolver.resolveResponseObject -> resolveResponseObject

    Args:
        full_name (str): Full name

    Returns:
        str: Method/Function name

    """
    point_pos = full_name.rfind('.')
    if point_pos != -1:
        return full_name[point_pos + 1:]
    else:
        return full_name


def replace_string_literal(source):
    """
    Replace the string literal in source code with ``<STR>``.

    Args:
        source (str): Source code in string

    Returns:
        str: Code after replaced

    """
    return re.sub(pattern=STRING_MATCHING_PATTERN, repl='___STR', string=source)


def remove_comments_and_docstrings(source, lang):
    """
    Remove docs and comments from source string.
    Thanks to authors of GraphCodeBERT
    from: https://github.com/microsoft/CodeBERT/blob/master/GraphCodeBERT/codesearch/parser/utils.py#L4

    Args:
        source (str): Source code string
        lang (str): Source code language

    Returns:
        str: Source string

    """
    if lang == enums.LANG_PYTHON:
        try:
            io_obj = StringIO(source)
            out = ""
            prev_token_type = tokenize.INDENT
            last_lineno = -1
            last_col = 0
            for tok in tokenize.generate_tokens(io_obj.readline):
                token_type = tok[0]
                token_string = tok[1]
                start_line, start_col = tok[2]
                end_line, end_col = tok[3]
                # l_text = tok[4]
                if start_line > last_lineno:
                    last_col = 0
                if start_col > last_col:
                    out += (" " * (start_col - last_col))
                # Remove comments:
                if token_type == tokenize.COMMENT:
                    pass
                # This series of conditionals removes docstrings:
                elif token_type == tokenize.STRING:
                    if prev_token_type != tokenize.INDENT:
                        # This is likely a docstring; double-check we're not inside an operator:
                        if prev_token_type != tokenize.NEWLINE:
                            if start_col > 0:
                                out += token_string
                else:
                    out += token_string
                prev_token_type = token_type
                last_col = end_col
                last_lineno = end_line
            temp = []
            for x in out.split('\n'):
                if x.strip() != "":
                    temp.append(x)
            return '\n'.join(temp)
        except Exception:
            return source
    elif lang in [enums.LANG_RUBY]:
        return source
    else:
        def replacer(match):
            s = match.group(0)
            if s.startswith('/'):
                return " "  # note: a space and not an empty string
            else:
                return s

        pattern = re.compile(
            r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
            re.DOTALL | re.MULTILINE
        )
        temp = []
        for x in re.sub(pattern, replacer, source).split('\n'):
            if x.strip() != "":
                temp.append(x)
        return '\n'.join(temp)


def parse_json_file(file, lang):
    """
    Parse a dataset file where each line is a json string representing a sample.

    Args:
        file (str): The file path
        lang (str): Source code language

    Returns:
        (list[str], list[str], list[str], list[str], List[str]):
            - List of source codes
            - List of tokenized codes
            - List of split method names
            - List of tokenized codes with method name replaced with ``f``
            - List of docstring strings, not every sample has it

    """
    sources = []
    codes = []
    names = []
    codes_wo_name = []
    docs = []
    with open(file, encoding='utf-8') as f:
        for line in f.readlines():
            data = json.loads(line.strip())
            name = trim_method_name(data['func_name'])
            source = data['code'].strip()
            source = remove_comments_and_docstrings(source, lang)
            source = replace_string_literal(source)
            code = replace_string_literal(' '.join(data['code_tokens']))

            sources.append(source)
            codes.append(code)

            code_wo_name = code.replace(name, 'f', 1)
            codes_wo_name.append(code_wo_name)

            name = ' '.join(split_identifier(name))
            names.append(name)

            if 'docstring' in data:
                doc = clean_doc(data['docstring'])
                if doc:
                    docs.append(doc)

    return sources, codes, names, codes_wo_name, docs


def iter_all_files(base):
    """
    Iterator for all file paths in the given base path.

    Args:
        base (str): Path like string

    Returns:
        str: Path of each file
    """
    for root, ds, fs in os.walk(base):
        for f in fs:
            yield os.path.join(root, f)


def iter_pre_train_dataset_files(lang_dir, lang):
    """
    Get files for pre-training, all files with extension ``jsonl`` will be included.

    Args:
        lang_dir (str): Path of language dir
        lang (str): Source code language

    Returns:
        list[str]: List of paths of files

    """
    # if lang in [enums.LANG_PYTHON]:
    #     for file in iter_all_files(base=lang_dir):
    #         if file.endswith('.jsonl'):
    #             return [file]
    # if lang in [enums.LANG_PYTHON]:
    #     return [file for file in iter_all_files(base=lang_dir) if file.endswith('.jsonl')]
    if lang in [enums.LANG_GO, enums.LANG_JAVA, enums.LANG_PYTHON, enums.LANG_JAVASCRIPT, enums.LANG_PHP,
                enums.LANG_RUBY]:
        return [file for file in iter_all_files(base=lang_dir) if file.endswith('.jsonl')]
    return []


def load_pre_train_dataset(file, lang):
    """
    Load json dataset from given file.

    Args:
        file (str): Path of dataset file
        lang (str): Source code language

    Returns:
        (list[str], list[str], list[str], list[str], list[str]):
            - List of source code strings
            - List of tokenized code strings
            - List of nl strings
            - List of tokenized code strings with method names replaced
            - List of doc strings, not every sample has it

    """
    if lang in [enums.LANG_JAVA, enums.LANG_PYTHON, enums.LANG_GO,
                enums.LANG_JAVASCRIPT, enums.LANG_PHP, enums.LANG_RUBY]:
        sources, codes, names, codes_wo_name, docs = parse_json_file(file, lang=lang)
        return sources, codes, names, codes_wo_name, docs


def load_dataset_from_dir(dataset_dir):
    """
    Load all files in the given dir, only for pre-training.

    Args:
        dataset_dir (str): Root directory

    Returns:
        (dict, list[str], list[str], list[str], List[str], list[str], list[str], list[str], list[str], list[str]):
            - Dict of paths: key is the dataset group, value is the path
            - List of str: languages for each line
            - List of str: source code
            - List of str: tokenized code string
            - List of ast: linearized ast string
            - List of str: split method name string
            - List of str:
            - List of str:
            - List of str:
            - List of str: List of docs

    """
    paths = {}
    languages = []
    all_sources = []
    all_asts = []
    all_codes = []
    all_codes_wo_name = []
    all_names = []
    all_names_wo_name = []
    all_only_names = []
    all_docs = []
    for file in os.listdir(dataset_dir):

        path = os.path.join(dataset_dir, file)
        if os.path.isfile(path):
            continue

        lang = file
        dataset_files = iter_pre_train_dataset_files(path, lang=lang)
        if len(dataset_files) > 0:
            logger.info(f'  Language: {lang}')
            paths[lang] = dataset_files
            n_sample = 0
            for dataset_file_path in dataset_files:
                sources, codes, names, codes_wo_name, docs = load_pre_train_dataset(file=dataset_file_path,
                                                                                    lang=lang)

                new_sources = []
                new_codes = []
                new_codes_wo_name = []
                new_names = []
                new_names_wo_name = []
                only_names = []
                asts = []
                for source, code, name, code_wo_name in tqdm(zip(sources, codes, names, codes_wo_name),
                                                             desc=f'Parsing {os.path.basename(dataset_file_path)}',
                                                             leave=False,
                                                             total=len(sources)):
                    try:
                        ast, nl, nl_wo_name = generate_single_ast_nl(source=source,
                                                                     lang=lang,
                                                                     name=name,
                                                                     replace_method_name=True)
                        new_sources.append(source)
                        new_codes.append(code)
                        new_codes_wo_name.append(code_wo_name)
                        new_names.append(nl)
                        new_names_wo_name.append(nl_wo_name)
                        asts.append(ast)
                        only_names.append(name)
                    except Exception:
                        continue

                all_sources += new_sources
                all_codes += new_codes
                all_codes_wo_name += new_codes_wo_name
                all_names += new_names
                all_names_wo_name += new_names_wo_name
                all_only_names += only_names
                all_asts += asts
                all_docs += docs

                n_line = len(new_sources)
                languages += [lang for _ in range(n_line)]
                n_sample += n_line

                logger.info(f'    File: {dataset_file_path}, {n_line} samples')

            logger.info(f'  {lang} dataset size: {n_sample}')

    assert len(languages) == len(all_sources) == len(all_codes) == len(all_codes_wo_name) == len(all_asts) == \
           len(all_names) == len(all_names_wo_name) == len(all_only_names)
    return paths, languages, all_sources, all_codes, all_asts, all_names, all_codes_wo_name, all_names_wo_name, \
           all_only_names, all_docs


def trim_spaces(string):
    """
    Replace consecutive spaces with a single whitespace.

    Args:
        string (str): String

    Returns:
        str: Replaced string
    """
    return re.sub(r'\s+', ' ', string).strip()


def tokenize_python(source):
    """
    Python lib to tokenize python source code.

    Args:
        source (str): Source code string

    Returns:
        str: Tokenized code string

    """
    tokens = tokenize.generate_tokens(StringIO(source).readline)
    return ' '.join([token.string for token in tokens if token.string.strip() != ''])


def tokenize_source(source, lang, use_regular=False):
    """
    Tokenize the source code into tokens.

    Args:
        source (str): Source in string
        lang (str): Language of source code
        use_regular (bool): Whether to use regular tokenize method, default to False

    Returns:
        str: Tokenized code, delimited by whitespace, string literal will be replaced by ``___STR``

    """
    if use_regular:
        code = replace_string_literal(regular_tokenize(source))
        return trim_spaces(code)
    if lang == enums.LANG_PYTHON:
        tokens = tokenize.generate_tokens(StringIO(source).readline)
        code = ' '.join([token.string for token in tokens])
        code = replace_string_literal(code)
        return trim_spaces(code)
    if lang in [enums.LANG_JAVA, enums.LANG_JAVASCRIPT, enums.LANG_PHP, enums.LANG_GO]:
        input_stream = InputStream(source)
        lexer = MAPPING_LANG_LEXER[lang](input_stream)
        tokens = [token.text for token in lexer.getAllTokens()]
        code = replace_string_literal(' '.join(tokens))
        return trim_spaces(code)
    elif lang == enums.LANG_RUBY:
        tokens = MAPPING_LANG_LEXER[lang].get_pure_tokens(source)
        code = replace_string_literal(' '.join([token[0] for token in tokens]))
        return trim_spaces(code)
    else:
        # TODO: c# tokenize
        code = replace_string_literal(regular_tokenize(source))
        return trim_spaces(code)


def count_non_space_chars(s):
    """
    Count the non-space characters.

    Args:
        s (str): String to be counted

    Returns:
        int: Number of non-space characters

    """
    matches = re.findall(NON_SPACE_MATCHING_PATTERN, s)
    return len(matches)


def align_source_code(former_source, code):
    """
    Align former source to code token string and split code into former one and latter one.

    Args:
        former_source (str): Former part of the source
        code (str): Tokenized source code

    Returns:
        (str, str):
            - Former part of tokenized code
            - Latter part of tokenized code

    """
    former_count = count_non_space_chars(former_source)
    total = 0
    code_tokens = code.split(' ')
    token_index = 0
    while total < former_count:
        total += count_non_space_chars(code_tokens[token_index])
        token_index += 1
    former_code = ' '.join(code_tokens[:token_index])
    latter_code = ' '.join(code_tokens[token_index:])
    return former_code, latter_code


def regular_tokenize(source: str):
    """
    NLTK word tokenize with simple adoptions for source code.

    Args:
        source (str): Source code string.

    Returns:
        str: Tokenized code string
    """
    source = re.sub(r'(\S)[.=](\S)', r'\1 . \2', source)
    return ' '.join(nltk.word_tokenize(source))


def clean_doc(s):
    """
    Clean docstring.

    Args:
        s (str): Raw docstring

    Returns:
        str: Cleaned docstring

    """
    # // Create an instance of  {@link RepresentationBaseType } and {@link RepresentationBaseType }.
    # // Create an instance of RepresentationBaseType and RepresentationBaseType
    # // Public setter for the  {@code rowMapper}.
    # // Public setter for the rowMapper
    # comment = comment.replaceAll("\\{@link|code(.*?)}", "$1");
    # comment = comment.replaceAll("@see", "");

    s = re.sub(r'{@link|code(.*?)}', r'\1', s)
    s = re.sub(r'@see', '', s)

    # // Implementation of the <a href="http://www.tarsnap.com/scrypt/scrypt.pdf"/>scrypt KDF</a>.
    # // Implementation of the scrypt KDF
    # comment = comment.replaceAll("<a.*?>(.*?)a>", "$1");
    s = re.sub(r'<a.*?>(.*?)a>', r'\1', s)

    # // remove all tags like <p>, </b>
    # comment = comment.replaceAll("</?[A-Za-z0-9]+>", "");
    s = re.sub(r'</?[A-Za-z0-9]+>', '', s)

    # // Set the list of the watchable objects (meta data).
    # // Set the list of the watchable objects
    # comment = comment.replaceAll("\\(.*?\\)", "");
    s = re.sub(r'\(.*?\)', '', s)

    # // #dispatchMessage dispatchMessage
    # // dispatchMessage
    # comment = comment.replaceAll("#([\\w]+)\\s+\\1", "$1");
    s = re.sub(r'#([\w]+)\s+\1', r'\1', s)

    # // remove http url
    # comment = comment.replaceAll("http\\S*", "");
    s = re.sub(r'http\S*', '', s)

    # // characters except english and number are ignored.
    # comment = comment.replaceAll("[^a-zA-Z0-9_]", " ");
    s = re.sub(r'[^a-zA-Z0-9_]', ' ', s)

    # // delete empty symbols
    # comment = comment.replaceAll("[ \f\n\r\t]", " ").trim();
    # comment = comment.replaceAll(" +", " ");
    s = re.sub(r'[ \f\n\r\t]', ' ', s).strip()
    s = re.sub(r' +', ' ', s).strip()

    if len(s) == 0 or len(s.split()) < 3:
        return None
    else:
        return s


def convert_python_source_classical_summarization(source: str):
    source = re.sub(r' *DCNL *', '\n', source)
    source = re.sub(r' *DCSP *', '\t', source)
    return source


def parse_for_summarization(source_path, code_path, nl_path, lang):
    """
    Load and parse dataset for code summarization.

    Args:
        source_path (str): Path of source code dataset
        code_path (str): Path of tokenized code dataset, if not file not exist, tokenize on the fly
        nl_path (str): Path of comment dataset
        lang (str): Source code language

    Returns:
        (Dict, list[str], list[str], list[str], list[str]):
            - Dict mapping dataset groups to paths
            - List of tokenized code strings
            - List of linearized AST strings
            - List of name and API sequence strings
            - List of comment strings

    """
    paths = {'source': source_path}
    logger.info(f'    Source code file: {source_path}')
    sources = load_lines(source_path)
    # if lang == enums.LANG_PYTHON:
    #     sources = [convert_python_source_classical_summarization(source) for source in sources]

    if not os.path.isfile(code_path):
        paths['code'] = source_path
        logger.info('    Tokenize source code')
        codes = [tokenize_source(source, lang=lang) for source in sources]
    else:
        paths['code'] = code_path
        logger.info(f'    Tokenized code file: {code_path}')
        codes = load_lines(code_path)
    paths['nl'] = nl_path
    logger.info(f'    Summarization file: {nl_path}')
    nls = load_lines(nl_path)
    # sources, codes, nls = sources[:1000], codes[:1000], nls[:1000]
    assert len(sources) == len(codes) == len(nls)

    new_codes = []
    new_nls = []
    names = []
    asts = []
    for source, code, nl in tqdm(zip(sources, codes, nls), desc='Parsing', leave=False, total=len(sources)):
        try:
            source = remove_comments_and_docstrings(source, lang=lang)
            ast, name = generate_single_ast_nl(source=source, lang=lang)
            new_codes.append(code)
            new_nls.append(nl)
            names.append(name)
            asts.append(ast)
        except Exception:
            continue

    return paths, new_codes, asts, names, new_nls


def parse_for_translation(source_path, source_lang, target_path, target_lang):
    """
    Load and parse for code translation.

    Args:
        source_path (str): Path of source dataset
        source_lang (str): Source language
        target_path (str): Path of target dataset
        target_lang (str): Target language

    Returns:
        (list[str], list[str], list[str], list[str]):
            - List of tokenized code strings
            - List of linearized AST strings
            - List of name and API sequence strings
            - List of tokenized target code strings

    """
    logger.info(f'    Source file: {source_path}')
    sources = load_lines(source_path)
    logger.info(f'    Target file: {target_path}')
    targets = load_lines(target_path)

    new_sources = []
    new_targets = []
    asts = []
    names = []
    for source, target in tqdm(zip(sources, targets), desc='Parsing', leave=False, total=len(sources)):
        try:
            source = remove_comments_and_docstrings(source, lang=source_lang)
            source = replace_string_literal(source)
            target = remove_comments_and_docstrings(target, lang=target_lang)
            target = replace_string_literal(target)

            ast, name = generate_single_ast_nl(source=source, lang=source_lang)
            code = tokenize_source(source=source, lang=source_lang, use_regular=True)
            tokenized_target = tokenize_source(source=target, lang=target_lang, use_regular=True)

            new_sources.append(code)
            asts.append(ast)
            names.append(name)
            new_targets.append(tokenized_target)
        except Exception:
            continue
    return new_sources, asts, names, new_targets


def parse_for_search(dataset_dir, lang, split):
    """
    Load and parse for code search.

    Args:
        dataset_dir (str): Directory of the dataset
        lang (str): Source code language
        split (str): Split set of the dataset, support `train`, `valid`, `test`, `codebase`

    Returns:
        (list[str], list[str], list[str], list[str])
            - List of tokenized code strings
            - List of AST sequences
            - List of name strings
            - List of nl strings

    """
    urls = []
    codes = []
    asts = []
    names = []
    nls = []

    path = os.path.join(dataset_dir, f'{split}.jsonl')
    with open(path, encoding='utf-8') as f:
        logger.info(f'  File: {path}')
        for line in tqdm(f.readlines()):
            data = json.loads(line.strip())
            if split in ['train', 'valid', 'test']:
                if 'docstring' not in data:
                    continue
                nl = clean_doc(data['docstring'])
                if nl is None:
                    continue
            try:
                if split in ['codebase', 'train']:
                    code = replace_string_literal(' '.join(data['code_tokens']))
                    name = trim_method_name(data['func_name'])

                    source = data['code'].strip()
                    source = remove_comments_and_docstrings(source, lang)
                    source = replace_string_literal(source)
                    ast, name = generate_single_ast_nl(source=source, lang=lang, name=name)

                    codes.append(code)
                    asts.append(ast)
                    names.append(name)

                if split in ['train', 'valid', 'test']:
                    nls.append(nl)

                if split != 'train':
                    url = data['url']
                    urls.append(url)
            except Exception:
                continue

    if split == 'codebase':
        return urls, codes, asts, names
    elif split == 'train':
        return codes, asts, names, nls
    elif split in ['valid', 'test']:
        return urls, nls


def load_clone_mapping(dataset_root):
    """
    Load json file and transfer to a mapping from code id to source code.

    Args:
        dataset_root (str): Root of the dataset

    Returns:
        dict: Mapping from code id to source code

    """
    path = os.path.join(dataset_root, 'fine_tune', enums.TASK_CLONE_DETECTION, 'data.jsonl')
    if not os.path.exists(path):
        return None
    mapping = dict()
    with open(path, encoding='utf-8') as f:
        for line in f.readlines():
            data = json.loads(line.strip())
            code_id = data['idx']
            source = data['func'].strip()
            mapping[code_id] = source
    return mapping


def parse_for_clone(path, mapping):
    """
    Load and parse for code clone detection.

    Args:
        path (str): Dataset path
        mapping (dict[int, str]): Mapping from code id to source code

    Returns:
        list[str], list[str], list[str], list[str], list[str], list[str], list[int]:
            - List of source code 1 strings
            - List of ast 1 strings
            - List of name 1 strings
            - List of source code 2 strings
            - List of ast 2 strings
            - List of name 2 strings
            - List of label integers

    """
    codes_1 = []
    asts_1 = []
    names_1 = []
    codes_2 = []
    asts_2 = []
    names_2 = []
    labels = []
    with open(path, encoding='utf-8') as f:
        for line in tqdm(f.readlines()):
            id_1, id_2, label = line.split('\t')
            try:
                source_1 = mapping[id_1]
                source_1 = remove_comments_and_docstrings(source_1, lang=enums.LANG_JAVA)
                source_1 = replace_string_literal(source_1)
                ast_1, name_1 = generate_single_ast_nl(source=source_1, lang=enums.LANG_JAVA)
                code_1 = tokenize_source(source=source_1, lang=enums.LANG_JAVA)

                source_2 = mapping[id_2]
                source_2 = remove_comments_and_docstrings(source_2, lang=enums.LANG_JAVA)
                source_2 = replace_string_literal(source_2)
                ast_2, name_2 = generate_single_ast_nl(source=source_2, lang=enums.LANG_JAVA)
                code_2 = tokenize_source(source=source_2, lang=enums.LANG_JAVA)

                label = int(label)

                codes_1.append(code_1)
                asts_1.append(ast_1)
                names_1.append(name_1)
                codes_2.append(code_2)
                asts_2.append(ast_2)
                names_2.append(name_2)
                labels.append(label)
            except Exception:
                continue
    return codes_1, asts_1, names_1, codes_2, asts_2, names_2, labels


def parse_for_completion(source_path, target_path):
    """
    Load and parse for code completion.

    Args:
        source_path (str): Path of source
        target_path (str): Path of target

    Returns:
        (list[str], list[str], list[str], list[str]):
            - List of strings: source code
            - List of strings: AST sequence
            - List of strings: name sequence
            - List of strings: target code

    """
    def restore_source(sub_source):
        """
        Transfer split source to source code, which can be parsed into AST.

        Args:
            sub_source (str): Split code

        Returns:
            str: Source code that can be parsed

        """
        tokens = sub_source.split()
        is_subtoken = False
        restored_source = ''
        for token in tokens:
            if token == '_':
                is_subtoken = True
                continue
            if token == 'PRED':
                token = Vocab.MSK_TOKEN
            if is_subtoken:
                restored_source += token.capitalize()
            else:
                restored_source += f' {token}'
            is_subtoken = False
        return restored_source.strip()

    source_lines = load_lines(source_path)
    target_lines = load_lines(target_path)
    assert len(source_lines) == len(target_lines)

    codes = []
    asts = []
    names = []
    targets = []
    for source, target in tqdm(zip(source_lines, target_lines), desc='Parsing', total=len(source_lines)):
        try:
            source = restore_source(source)
            target = restore_source(target)
            ast, name = generate_single_ast_nl(source=source, lang=enums.LANG_JAVA)
            codes.append(source)
            asts.append(ast)
            names.append(name)
            targets.append(target)
        except Exception:
            continue
    return codes, asts, names, targets


def parse_for_bug_fix(buggy_path, fixed_path):
    """
    Load and parse for bug fix.

    Args:
        buggy_path (str): Path of buggy code
        fixed_path (str): Path of fixed code

    Returns:
        (list[str], list[str], list[str], list[str]):
            - List of strings: source code
            - List of strings: AST sequence
            - List of strings: name sequence
            - List of strings: target code

    """
    buggy_lines = load_lines(buggy_path)
    fixed_lines = load_lines(fixed_path)
    assert len(buggy_lines) == len(fixed_lines)
    codes = []
    asts = []
    names = []
    targets = []
    for buggy, fixed in tqdm(zip(buggy_lines, fixed_lines), desc='Parsing', total=len(buggy_lines)):
        try:
            ast, name = generate_single_ast_nl(source=buggy, lang=enums.LANG_JAVA)
            codes.append(buggy.lower())
            asts.append(ast)
            names.append(name.lower())
            targets.append(fixed.lower())
        except Exception:
            continue
    return codes, asts, names, targets
