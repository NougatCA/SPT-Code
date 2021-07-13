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


def load_lines(path):
    """
    Load lines from given path.

    Args:
        path (str): Dataset file path

    Returns:
        list: List of lines

    """
    with open(path, encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]
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
        (list[str], list[str], list[str], list[str]):
            - List of source codes
            - List of tokenized codes
            - List of split method names
            - List of tokenized codes with method name replaced with ``f``

    """
    sources = []
    codes = []
    names = []
    codes_wo_name = []
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

    return sources, codes, names, codes_wo_name


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
    if lang in [enums.LANG_GO, enums.LANG_JAVA, enums.LANG_PYTHON, enums.LANG_JAVASCRIPT, enums.LANG_PHP, enums.LANG_RUBY]:
    # if lang in [vars.LANG_JAVASCRIPT]:
        return [file for file in iter_all_files(base=lang_dir) if file.endswith('.jsonl')]
    return []


def load_pre_train_dataset(file, lang):
    """
    Load json dataset from given file.

    Args:
        file (str): Path of dataset file
        lang (str): Source code language

    Returns:
        (list[str], list[str], list[str], list[str]):
            - List of source code strings
            - List of tokenized code strings
            - List of nl strings
            - List of tokenized code strings with method names replaced

    """
    if lang in [enums.LANG_JAVA, enums.LANG_PYTHON, enums.LANG_GO, enums.LANG_JAVASCRIPT, enums.LANG_PHP, enums.LANG_RUBY]:
        sources, codes, names, codes_wo_name = parse_json_file(file, lang=lang)
        return sources, codes, names, codes_wo_name


def load_dataset_from_dir(dataset_dir):
    """
    Load all files in the given dir, only for pre-training.

    Args:
        dataset_dir (str): Root directory

    Returns:
        (list[str], list[str], list[str], List[str], list[str], list[str], list[str], list[str]):
            - List of str: languages for each line
            - List of str: source code
            - List of str: tokenized code string
            - List of ast: linearized ast string
            - List of str: split method name string
            - List of str:
            - List of str:
            - List of str

    """

    languages = []
    all_sources = []
    all_asts = []
    all_codes = []
    all_codes_wo_name = []
    all_names = []
    all_names_wo_name = []
    all_only_names = []
    for file in os.listdir(dataset_dir):

        path = os.path.join(dataset_dir, file)
        if os.path.isfile(path):
            continue

        lang = file
        dataset_files = iter_pre_train_dataset_files(path, lang=lang)
        if len(dataset_files) > 0:
            logger.info(f'  Language: {lang}')
            n_sample = 0
            for dataset_file_path in dataset_files:

                logger.info(f'    File: {dataset_file_path}')
                sources, codes, names, codes_wo_name = load_pre_train_dataset(file=dataset_file_path,
                                                                              lang=lang)

                new_sources = []
                new_codes = []
                new_codes_wo_name = []
                new_names = []
                new_names_wo_name = []
                only_names = []
                asts = []
                for source, code, name, code_wo_name in tqdm(zip(sources, codes, names, codes_wo_name),
                                                             desc='Parsing',
                                                             leave=False):
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

                n_line = len(new_sources)
                languages += [lang for _ in range(n_line)]
                n_sample += n_line

            logger.info(f'  {lang} dataset size: {n_sample}')

    assert len(languages) == len(all_sources) == len(all_codes) == len(all_codes_wo_name) == len(all_asts) == \
           len(all_names) == len(all_names_wo_name) == len(all_only_names)
    return languages, all_sources, all_codes, all_asts, all_names, all_codes_wo_name, all_names_wo_name, all_only_names


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


def tokenize_source(source, lang):
    """
    Tokenize the source code into tokens.

    Args:
        source (str): Source in string
        lang (str): Language of source code

    Returns:
        str: Tokenized code, delimited by whitespace, string literal will be replaced by ``___STR``

    """
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


def parse_for_summarization(source_path, code_path, nl_path, lang):
    """
    Load and parse dataset for code summarization.

    Args:
        source_path (str): Path of source code dataset
        code_path (str): Path of tokenized code dataset, if not file not exist, tokenize on the fly
        nl_path (str): Path of comment dataset
        lang (str): Source code language

    Returns:
        (list[str], list[str], list[str], list[str]):
            - List of tokenized code strings
            - List of linearized AST strings
            - List of name and API sequence strings
            - List of comment strings

    """
    logger.info(f'    Source code file: {source_path}')
    sources = load_lines(source_path)

    if not os.path.isfile(code_path):
        logger.info('    Tokenize source code')
        codes = [tokenize_source(source, lang=lang) for source in sources]
    else:
        logger.info(f'    Tokenized code file: {code_path}')
        codes = load_lines(code_path)
    logger.info(f'    Summarization file: {nl_path}')
    nls = load_lines(nl_path)
    # sources, codes, nls = sources[:1000], codes[:1000], nls[:1000]
    assert len(sources) == len(codes) == len(nls)

    return codes, None, None, nls

    new_codes = []
    new_nls = []
    names = []
    asts = []
    for source, code, nl in tqdm(zip(sources, codes, nls), desc='Parsing', leave=False):
        try:
            source = remove_comments_and_docstrings(source, lang=lang)
            ast, name = generate_single_ast_nl(source=source, lang=lang)
            new_codes.append(code)
            new_nls.append(nl)
            names.append(name)
            asts.append(ast)
        except Exception:
            continue

    return new_codes, asts, names, new_nls


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
    for source, target in tqdm(zip(sources, targets), desc='Parsing', leave=False):
        try:
            source = remove_comments_and_docstrings(source, lang=source_lang)
            source = replace_string_literal(source)
            target = remove_comments_and_docstrings(target, lang=target_lang)
            target = replace_string_literal(target)

            ast, name = generate_single_ast_nl(source=source, lang=source_lang)
            code = tokenize_source(source=source, lang=source_lang)
            tokenized_target = tokenize_source(source=target, lang=target_lang)

            new_sources.append(code)
            asts.append(ast)
            names.append(name)
            new_targets.append(tokenized_target)
        except Exception:
            continue
    return new_sources, asts, names, new_targets


def parse_for_search(dataset_dir, lang):
    """
    Load and parse for code search.

    Args:
        dataset_dir (str): Directory of the dataset
        lang (str): Source code language

    Returns:
        (list[str], list[str], list[str], list[str])
            - List of tokenized code strings
            - List of AST sequences
            - List of name strings
            - List of nl strings

    """
    codes = []
    asts = []
    names = []
    nls = []
    for file in iter_all_files(dataset_dir):
        if not file.endswith('.jsonl'):
            continue
        with open(file, encoding='utf-8') as f:
            logger.info(f'  File: {file}')
            for line in tqdm(f.readlines()):
                data = json.loads(line.strip())
                if 'docstring_tokens' not in data:
                    continue
                try:
                    code = replace_string_literal(' '.join(data['code_tokens']))
                    name = trim_method_name(data['func_name'])

                    source = data['code'].strip()
                    source = remove_comments_and_docstrings(source, lang)
                    source = replace_string_literal(source)
                    ast, name = generate_single_ast_nl(source=source, lang=lang, name=name)

                    nl = ' '.join(data['docstring_tokens'])

                    codes.append(code)
                    asts.append(ast)
                    name = ' '.join(split_identifier(name))
                    names.append(name)
                    nls.append(nl)
                except Exception:
                    continue

        return codes, asts, names, nls
