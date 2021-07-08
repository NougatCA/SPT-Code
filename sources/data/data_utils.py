import re
import json
import os
import logging
import sctokenizer
from code_tokenizer.tokenizer import TokeNizer

from .asts.ast_parser import generate_single_ast_nl
import vars

logger = logging.getLogger(__name__)

STRING_MATCHING_PATTERN = re.compile(r'([bruf]*)(\"\"\"|\'\'\'|\"|\')(?:(?!\2)(?:\\.|[^\\]))*\2')

# map the language names between internal and ``code_tokenizer``
CODE_TOKENIZER_MAPPING = {vars.PYTHON_LANG: TokeNizer('Python'),
                          vars.JAVA_LANG: TokeNizer('Java'),
                          vars.JAVASCRIPT_LANG: TokeNizer('JavaScript'),
                          vars.RUBY_LANG: TokeNizer('Ruby'),
                          vars.GO_LANG: TokeNizer('Go'),
                          vars.PHP_LANG: TokeNizer('PHP')}


def camel_split(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    return [m.group(0) for m in matches]


def split_identifier(identifier):
    """
    Split identifier into a list of subtokens.
    Tokens except characters and digits will be eliminated.

    Args:
        identifier (str): given identifier

    Returns:
        list[str]: list of subtokens
    """
    words = []

    word = re.sub(r'[^a-zA-Z0-9]', ' ', identifier)
    word = re.sub(r'(\d+)', r' \1 ', word)
    split_words = word.strip().split()
    for split_word in split_words:
        camel_words = camel_split(split_word)
        for camel_word in camel_words:
            words.append(camel_word.lower())

    return words


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


def parse_json_file(file, replace_method_name=False):
    """
    Parse a dataset file where each line is a json string representing a sample.

    Args:
        file (str): The file path
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
            code = replace_string_literal(' '.join(data['code_tokens']))
            if replace_method_name:
                code = code.replace(name, 'f', 1)

            sources.append(source)
            codes.append(code)
            names.append(' '.join(split_identifier(name)))

    return sources, codes, names


def find_all_files(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            yield os.path.join(root, f)


def get_pre_train_dataset_files(lang_dir, lang):
    # if lang in ['go', 'java', 'python', 'javascript', 'php', 'ruby']:
    if lang in [vars.JAVA_LANG]:
        return [file for file in find_all_files(base=lang_dir) if file.endswith('.jsonl')]
    return None


def get_pre_train_dataset(file, lang, replace_method_name=False):
    if lang in [vars.JAVA_LANG, vars.PYTHON_LANG, vars.GO_LANG, vars.JAVASCRIPT_LANG, vars.PHP_LANG, vars.RUBY_LANG]:
        sources, codes, names = parse_json_file(file, replace_method_name)
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
        dataset_files = get_pre_train_dataset_files(path, lang=lang)
        if dataset_files and len(dataset_files) > 0:
            logger.info(f'Loading {lang} dataset')
            n_sample = 0
            for dataset_file_path in dataset_files:
                sources, codes, names = get_pre_train_dataset(file=dataset_file_path,
                                                              lang=lang,
                                                              replace_method_name=replace_method_name)

                new_sources = []
                new_codes = []
                new_names = []
                asts = []
                for source, code, name in zip(sources, codes, names):
                    try:
                        ast, nl = generate_single_ast_nl(source=source, lang=lang, name=name)
                        new_sources.append(source)
                        new_codes.append(code)
                        new_names.append(name)
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
        - str: Replaced string
    """
    return re.sub(r'\s+', ' ', string)


def tokenize_source(source, lang):
    """
    Tokenize the source code into tokens
    Args:
        source (str): Source in string
        lang (str): Language of source code

    Returns:
        str: Tokenized code, delimited by whitespace, string literal will be replaced by ``___STR``

    """
    if lang in [vars.PYTHON_LANG, vars.JAVA_LANG, vars.JAVASCRIPT_LANG, vars.RUBY_LANG, vars.GO_LANG, vars.PHP_LANG]:
        tokenizer = CODE_TOKENIZER_MAPPING[lang]
        tokens = tokenizer.getPureTokens(source)
        code = replace_string_literal(' '.join(tokens))
        return trim_spaces(code)
    elif lang in ['c', 'cpp', vars.JAVA_LANG, vars.PYTHON_LANG, vars.PHP_LANG]:
        tokens = sctokenizer.tokenize_str(source_str=source, lang=lang)
        code = replace_string_literal(' '.join([token.token_value for token in tokens]))
        return trim_spaces(code)
    # c#
    else:
        # TODO: c# tokenize
        return source[:]


def parse_for_summarization(source_path, code_path, nl_path, lang):
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
            ast, name = generate_single_ast_nl(source=source, lang=lang)
            new_codes.append(code)
            new_nls.append(nl)
            names.append(name)
            asts.append(ast)
        except Exception:
            continue

    return new_codes, asts, names, new_nls


def parse_for_translation(source_path, source_lang, target_path, target_lang):
    sources = load_lines(source_path)
    targets = load_lines(target_path)

    new_sources = []
    new_targets = []
    asts = []
    names = []
    for source, target in zip(sources, targets):
        try:
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
