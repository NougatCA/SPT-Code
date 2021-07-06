import re
import json
import os
import logging
import sctokenizer
from code_tokenizer.tokenizer import TokeNizer

from .asts.ast_parser import get_single_ast, get_single_ast_name

logger = logging.getLogger(__name__)

STRING_MATCHING_PATTERN = re.compile(r'([bruf]*)(\"\"\"|\'\'\'|\"|\')(?:(?!\2)(?:\\.|[^\\]))*\2')

# map the language names between internal and ``code_tokenizer``
CODE_TOKENIZER_MAPPING = {'python': TokeNizer('Python'),
                          'java': TokeNizer('Java'),
                          'javascript': TokeNizer('JavaScript'),
                          'ruby': TokeNizer('Ruby'),
                          'go': TokeNizer('Go'),
                          'php': TokeNizer('PHP')}


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


def get_method_name(full_name):
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


def parse_json_file(file):
    """
    Parse a dataset file where each line is a json string representing a sample.

    Args:
        file (str): The file path

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
            name = get_method_name(data['func_name'])
            source = data['code']
            code = replace_string_literal(' '.join(data['code_tokens']))

            sources.append(source)
            codes.append(code)
            names.append(' '.join(split_identifier(name)))

    return sources, codes, names


def find_all_files(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            yield os.path.join(root, f)


def get_pre_train_dataset_files(lang_dir, language):
    # if language in ['go', 'java', 'python', 'javascript', 'php', 'ruby']:
    if language in ['java']:
        return [file for file in find_all_files(base=lang_dir) if file.endswith('.jsonl')]
    return None


def get_pre_train_dataset(file, language):
    if language in ['go', 'java', 'python', 'javascript', 'php', 'ruby']:
        sources, codes, names = parse_json_file(file)
        return sources, codes, names


def load_dataset_from_dir(dataset_dir):
    """
    Load all files in the given dir

    Args:
        dataset_dir (str): Root directory

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
        dataset_files = get_pre_train_dataset_files(path, language=lang)
        if dataset_files and len(dataset_files) > 0:
            logger.info(f'Loading {lang} dataset')
            n_sample = 0
            for dataset_file_path in dataset_files:
                sources, codes, names = get_pre_train_dataset(file=dataset_file_path, language=lang)

                new_sources = []
                new_codes = []
                new_names = []
                asts = []
                for source, code, name in zip(sources, codes, names):
                    try:
                        ast = get_single_ast(language=lang, source=source)
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


def tokenize_source(source, language):
    """
    Tokenize the source code into tokens
    Args:
        source (str): Source in string
        language (str): Language of source code

    Returns:
        str: Tokenized code, delimited by whitespace, string literal will be replaced by ``___STR``

    """
    if language in ['python', 'java', 'javascript', 'ruby', 'go', 'php']:
        tokenizer = CODE_TOKENIZER_MAPPING[language]
        tokens = tokenizer.getPureTokens(source)
        code = replace_string_literal(' '.join(tokens))
        return trim_spaces(code)
    elif language in ['c', 'cpp', 'java', 'python', 'php']:
        tokens = sctokenizer.tokenize_str(source_str=source, lang=language)
        code = replace_string_literal(' '.join([token.token_value for token in tokens]))
        return trim_spaces(code)
    # c#
    else:
        return source[:]


def parse_for_summarization(source_path, code_path, nl_path, language):
    sources = load_lines(source_path)

    if not os.path.isfile(code_path):
        codes = [tokenize_source(source, language=language) for source in sources]
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
            ast, name = get_single_ast_name(language=language, source=source)
            new_codes.append(code)
            new_nls.append(nl)
            names.append(' '.join(split_identifier(name)))
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
            ast, name = get_single_ast_name(language=source_lang, source=source)
            code = tokenize_source(source=source, language=source_lang)
            tokenized_target = tokenize_source(source=target, language=target_lang)

            new_sources.append(code)
            asts.append(ast)
            names.append(' '.join(split_identifier(name)))
            new_targets.append(tokenized_target)
        except Exception:
            continue
    return new_sources, asts, names, new_targets
