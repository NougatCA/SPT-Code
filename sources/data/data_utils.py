import re
import tokenize
from io import StringIO
import json
import os
import logging
import sctokenizer
from data.code_tokenizer.tokenizer import TokeNizer

from .asts.ast_parser import generate_single_ast_nl
import vars

logger = logging.getLogger(__name__)

STRING_MATCHING_PATTERN = re.compile(r'([bruf]*)(\"\"\"|\'\'\'|\"|\')(?:(?!\2)(?:\\.|[^\\]))*\2')

# map the language names between internal and ``code_tokenizer``
CODE_TOKENIZER_MAPPING = {vars.LANG_PYTHON: TokeNizer('Python'),
                          vars.LANG_JAVA: TokeNizer('Java'),
                          vars.LANG_JAVASCRIPT: TokeNizer('JavaScript'),
                          vars.LANG_RUBY: TokeNizer('Ruby'),
                          vars.LANG_GO: TokeNizer('Go'),
                          vars.LANG_PHP: TokeNizer('PHP')}


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
    if lang == vars.LANG_PYTHON:

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
    elif lang in [vars.LANG_RUBY]:
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


def parse_json_file(file, lang, replace_method_name=False):
    """
    Parse a dataset file where each line is a json string representing a sample.

    Args:
        file (str): The file path
        lang (str): Source code language
        replace_method_name (bool): Whether to replace method names in codes, default to False

    Returns:
        (list[str], list[str], list[str]):
            - List of source codes
            - List of tokenized codes
            - List of split method names

    """
    sources = []
    codes = []
    names = []
    with open(file, encoding='utf-8') as f:
        for line in f.readlines():
            data = json.loads(line.strip())
            name = trim_method_name(data['func_name'])
            source = data['code']
            source = remove_comments_and_docstrings(source, lang)
            code = replace_string_literal(' '.join(data['code_tokens']))
            if replace_method_name:
                code = code.replace(name, 'f', 1)

            sources.append(source)
            codes.append(code)
            names.append(name)

    return sources, codes, names


def find_all_files(base):
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
    # if lang in ['go', 'java', 'python', 'javascript', 'php', 'ruby']:
    if lang in [vars.LANG_JAVA]:
        return [file for file in find_all_files(base=lang_dir) if file.endswith('.jsonl')]
    return []


def load_pre_train_dataset(file, lang, replace_method_name=False):
    """
    Load json dataset from given file.

    Args:
        file (str): Path of dataset file
        lang (str): Source code language
        replace_method_name (bool): Whether to replace method name, default to False

    Returns:
        (list[str], list[str], list[str]):
            - List of source code strings
            - List of tokenized code strings
            - List of nl strings
    """
    if lang in [vars.LANG_JAVA, vars.LANG_PYTHON, vars.LANG_GO, vars.LANG_JAVASCRIPT, vars.LANG_PHP, vars.LANG_RUBY]:
        sources, codes, names = parse_json_file(file, lang=lang, replace_method_name=replace_method_name)
        return sources, codes, names


def load_dataset_from_dir(dataset_dir, replace_method_name=False):
    """
    Load all files in the given dir

    Args:
        dataset_dir (str): Root directory
        replace_method_name (bool): Whether to replace method names in ``all_codes``, default to False

    Returns:
        (list[str], dict[str, int], list[str], list[str], List[str], list[str]):
            - List of str: languages for each line
            - Map the dir path to a list of filenames
            - List of str: source code
            - List of str: tokenized code string
            - List of ast: linearized ast string
            - List of str: split method name string

    """
    languages = []
    lang_lines = {}
    all_sources = []
    all_asts = []
    all_codes = []
    all_names = []
    for file in os.listdir(dataset_dir):

        path = os.path.join(dataset_dir, file)
        if os.path.isfile(path):
            continue

        lang = file
        dataset_files = iter_pre_train_dataset_files(path, lang=lang)
        if len(dataset_files) > 0:
            logger.info(f'Loading {lang} dataset')
            n_sample = 0
            for dataset_file_path in dataset_files:
                sources, codes, names = load_pre_train_dataset(file=dataset_file_path,
                                                               lang=lang,
                                                               replace_method_name=replace_method_name)

                new_sources = []
                new_codes = []
                new_names = []
                asts = []
                for source, code, name in zip(sources, codes, names):
                    try:
                        ast, nl = generate_single_ast_nl(source=source,
                                                         lang=lang,
                                                         name=name,
                                                         replace_method_name=replace_method_name)
                        new_sources.append(source)
                        new_codes.append(code)
                        new_names.append(nl)
                        asts.append(ast)
                    except Exception:
                        continue

                all_sources += new_sources
                all_codes += new_codes
                all_names += new_names
                all_asts += asts

                n_line = len(new_sources)
                languages += [lang for _ in range(n_line)]
                n_sample += n_line

            logger.info(f'{lang} dataset size: {n_sample}')
            lang_lines.update({lang: n_sample})

    assert len(languages) == len(all_sources) == len(all_codes) == len(all_asts)
    return languages, lang_lines, all_sources, all_codes, all_asts, all_names


def trim_spaces(string):
    """
    Replace consecutive spaces with a single whitespace.

    Args:
        string (str): String

    Returns:
        str: Replaced string
    """
    return re.sub(r'\s+', ' ', string)


def tokenize_source(source, lang):
    """
    Tokenize the source code into tokens.

    Args:
        source (str): Source in string
        lang (str): Language of source code

    Returns:
        str: Tokenized code, delimited by whitespace, string literal will be replaced by ``___STR``

    """
    if lang in [vars.LANG_PYTHON, vars.LANG_JAVA, vars.LANG_JAVASCRIPT, vars.LANG_RUBY, vars.LANG_GO, vars.LANG_PHP]:
        tokenizer = CODE_TOKENIZER_MAPPING[lang]
        tokens = tokenizer.getPureTokens(source)
        code = replace_string_literal(' '.join(tokens))
        return trim_spaces(code)
    elif lang in ['c', 'cpp', vars.LANG_JAVA, vars.LANG_PYTHON, vars.LANG_PHP]:
        tokens = sctokenizer.tokenize_str(source_str=source, lang=lang)
        code = replace_string_literal(' '.join([token.token_value for token in tokens]))
        return trim_spaces(code)
    # c#
    else:
        # TODO: c# tokenize
        return source[:]


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
    sources = load_lines(source_path)

    if not os.path.isfile(code_path):
        codes = [tokenize_source(source, lang=lang) for source in sources]
    else:
        codes = load_lines(code_path)
    nls = load_lines(nl_path)
    assert len(sources) == len(codes) == len(nls)

    new_codes = []
    new_nls = []
    names = []
    asts = []
    for source, code, nl in zip(sources, codes, nls):
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
    sources = load_lines(source_path)
    targets = load_lines(target_path)

    new_sources = []
    new_targets = []
    asts = []
    names = []
    for source, target in zip(sources, targets):
        try:
            source = remove_comments_and_docstrings(source, lang=source_lang)
            target = remove_comments_and_docstrings(target, lang=target_lang)

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
