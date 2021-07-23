
import tree_sitter
from tree_sitter import Language, Parser
import re

import enums


LANGUAGE = {enums.LANG_GO: Language('data/asts/build/my-languages.so', 'go'),
            enums.LANG_JAVASCRIPT: Language('data/asts/build/my-languages.so', 'javascript'),
            enums.LANG_PYTHON: Language('data/asts/build/my-languages.so', 'python'),
            enums.LANG_JAVA: Language('data/asts/build/my-languages.so', 'java'),
            enums.LANG_PHP: Language('data/asts/build/my-languages.so', 'php'),
            enums.LANG_RUBY: Language('data/asts/build/my-languages.so', 'ruby'),
            enums.LANG_C_SHARP: Language('data/asts/build/my-languages.so', 'c_sharp')}

# LANGUAGE = {enums.LANG_GO: Language('build/my-languages.so', 'go'),
#             enums.LANG_JAVASCRIPT: Language('build/my-languages.so', 'javascript'),
#             enums.LANG_PYTHON: Language('build/my-languages.so', 'python'),
#             enums.LANG_JAVA: Language('build/my-languages.so', 'java'),
#             enums.LANG_PHP: Language('build/my-languages.so', 'php'),
#             enums.LANG_RUBY: Language('build/my-languages.so', 'ruby'),
#             enums.LANG_C_SHARP: Language('build/my-languages.so', 'c_sharp')}

parser = Parser()

SOURCE_PREFIX_POSTFIX = {
    enums.LANG_PHP: ['<?php ', ' ?>'],
    enums.LANG_JAVA: ['class A{ ', ' }']
}

PATTERNS_METHOD_ROOT = {
    enums.LANG_JAVA: """
    (program
        (class_declaration
            body: (class_body
                (method_declaration) @method_root)
        )
    )
    """
}

PATTERNS_METHOD_BODY = {
    enums.LANG_JAVA: """
    (method_declaration
        body: (block) @body
    )
    """,

    enums.LANG_JAVASCRIPT: """
    (program
        (function_declaration
            body: (statement_block) @body
        )
    )
    """,

    enums.LANG_GO: """
    (source_file
        [
        (function_declaration
            body: (block) @body)

        (method_declaration
            body: (block) @body)
        ]
    )
    """
}

PATTERNS_METHOD_NAME = {
    enums.LANG_JAVA: """
    (method_declaration
        name: (identifier) @method_name
    )
    """,

    enums.LANG_PYTHON: """
    (module
        (function_definition
            name: (identifier) @method_name
        )
    )
    """,

    enums.LANG_GO: """
    [
        (source_file
            (method_declaration
                name: (field_identifier) @method_name
            )
        )
        (source_file
            (function_declaration
                name: (identifier) @method_name
            )
        )
    ]
    """,

    enums.LANG_JAVASCRIPT: """
    (program
        (function_declaration
            name: (identifier) @method_name
        )
    )
    """,

    enums.LANG_RUBY: """
    (program
        (method
            name: (identifier) @method_name
        )
    )
    """,

    enums.LANG_PHP: """
    (program
        (function_definition
            name: (name) @method_name
        )
    )
    """
}

PATTERNS_METHOD_INVOCATION = {
    enums.LANG_JAVA: """
    (method_invocation
        name: (identifier) @method_invocation
    )
    """,

    enums.LANG_PYTHON: """
    [
        (call
            function: (identifier) @method_invocation
        )
        (call
            function: (attribute
                attribute: (identifier) @method_invocation
            )
        )
    ]
    """,

    enums.LANG_GO: """
    [
        (call_expression
            function: (selector_expression
                field: (field_identifier) @method_invocation
            )
        )
        (call_expression
            function: (identifier) @method_invocation
        )
    ]
    """,

    enums.LANG_JAVASCRIPT: """
    [
        (call_expression
            function: (member_expression
                property: (property_identifier) @method_invocation
            )
        )
        (call_expression
            function: (identifier) @method_invocation
        )
    ]
    """,

    enums.LANG_RUBY: """
    (call
        method: (identifier) @method_invocation
    )
    """,

    enums.LANG_PHP: """
    [
        (scoped_call_expression
            name: (name) @method_invocation
        )
        (function_call_expression
            (name) @method_invocation
        )
        (member_call_expression
            name: (name) @method_invocation
        )
        (object_creation_expression
            (qualified_name
                (name) @method_invocation
            )
        )
    ]
    """
}

STATEMENT_ENDING_STRINGS = {
    enums.LANG_JAVA: ['statement', 'expression', 'declaration'],
    enums.LANG_PYTHON: ['statement', 'assignment'],
    enums.LANG_GO: ['statement', 'declaration', 'expression'],
    enums.LANG_JAVASCRIPT: ['statement', 'expression'],
    enums.LANG_RUBY: ['call', 'assignment', 'if', 'unless_modifier', 'operator_assignment', 'if_modifier', 'return',
                      'rescue', 'else', 'unless', 'when', 'for', 'while_modifier', 'until'],
    enums.LANG_PHP: ['statement', 'expression']
}


# ELIMINATE_AST_NODE = ['(', ')', '{', '}', ';']


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


def parse_ast(source, lang):
    """
    Parse the given code into corresponding ast.
    Args:
        source (str): code in string
        lang (str): Set the language

    Returns:
        tree_sitter.Node: Method/Function root node

    """
    parser.set_language(LANGUAGE[lang])
    if lang in SOURCE_PREFIX_POSTFIX:
        source = SOURCE_PREFIX_POSTFIX[lang][0] + source + SOURCE_PREFIX_POSTFIX[lang][1]
    tree = parser.parse(source.encode('utf-8').decode('unicode_escape').encode())
    root = tree.root_node
    # tree = parser.parse(str.encode(source))
    if lang in PATTERNS_METHOD_ROOT:
        query = LANGUAGE[lang].query(PATTERNS_METHOD_ROOT[lang])
        captures = query.captures(root)
        root = captures[0][0]
    return root


def get_node_name(source, node, lang):
    """
    Get node name, for php is shifted by prefix.

    Args:
        source (str): Source code string
        node (tree_sitter.Node): Node instance
        lang (str): Source code language

    Returns:
        str: Name of node

    """
    if node.is_named:
        if lang in SOURCE_PREFIX_POSTFIX:
            return source[node.start_byte - len(SOURCE_PREFIX_POSTFIX[lang][0]):
                          node.end_byte - len(SOURCE_PREFIX_POSTFIX[lang][0])]
        else:
            return source[node.start_byte: node.end_byte]
    return ''


def get_method_name(source, root, lang):
    """
    Return the name of method/function.

    Args:
        source (str): Source code string
        root (tree_sitter.Node): Method/Function root node
        lang (str): Source code language

    Returns:

    """
    query = LANGUAGE[lang].query(PATTERNS_METHOD_NAME[lang])
    captures = query.captures(root)
    if len(captures) == 0:
        return ''
    return get_node_name(source, captures[0][0], lang)


# def get_xsbt(source, node):
#     xsbt = []
#     if len(node.children) == 0:
#         if get_node_name(source, node) not in ELIMINATE_AST_NODE and \
#            node.type not in ELIMINATE_AST_NODE:
#             xsbt.append(node.type)
#     else:
#         xsbt.append(f'<{node.type}>')
#         len_before = len(xsbt)
#         for child in node.children:
#             xsbt += get_xsbt(source, child)
#         if len_before == len(xsbt) and len_before != 0:
#             xsbt[-1] = node.type
#         else:
#             xsbt.append(f'</{node.type}>')
#     return xsbt


def is_statement_node(node, lang):
    """
    Return whether the node is a statement level node.

    Args:
        node (tree_sitter.Node): Node to be queried
        lang (str): Source code language

    Returns:
        bool: True if given node is a statement node

    """
    endings = STATEMENT_ENDING_STRINGS[lang]
    end = node.type.split('_')[-1]
    if end in endings:
        return True
    else:
        return False


def get_node_type(node, lang):
    """
    Return the type of node, for ruby, add ``_statement`` to the end.

    Args:
        node (tree_sitter.Node): Node to be queried
        lang (str): Source code language

    Returns:
        str: Type of the node

    """
    return f'{node.type}_statement' if lang == enums.LANG_RUBY else node.type


def __statement_xsbt(node, lang):
    """
    Method used to generate X-SBT recursively.

    Args:
        node (tree_sitter.Node): Root node to traversal
        lang (str): Source code language

    Returns:
        list[str]: List of strings representing node types

    """
    xsbt = []

    if len(node.children) == 0:
        if is_statement_node(node, lang):
            xsbt.append(get_node_type(node, lang))
    else:
        if is_statement_node(node, lang):
            xsbt.append(f'{get_node_type(node, lang)}__')
        len_before = len(xsbt)
        for child in node.children:
            xsbt += __statement_xsbt(node=child, lang=lang)
        if len_before == len(xsbt) and len_before != 0:
            xsbt[-1] = get_node_type(node, lang)
        elif is_statement_node(node, lang):
            xsbt.append(f'__{get_node_type(node, lang)}')

    return xsbt


def generate_statement_xsbt(node, lang):
    """
    Generate X-SBT string.

    Args:
        node (tree_sitter.Node): Root node to traversal
        lang (str): Source code language

    Returns:
        str: X-SBT string

    """
    if lang in PATTERNS_METHOD_BODY:
        query = LANGUAGE[lang].query(PATTERNS_METHOD_BODY[lang])
        captures = query.captures(node)
        node = captures[0][0]
    tokens = __statement_xsbt(node=node, lang=lang)
    return ' '.join(tokens)


def extract_method_invocation(source, root, lang):
    """
    Extract method invocation sequence from given root.

    Args:
        source (str): Source code string
        root (tree_sitter.Node): Node to be extracted from
        lang (str): Source code language

    Returns:
        list[str]: List of method invocation strings

    """
    query = LANGUAGE[lang].query(PATTERNS_METHOD_INVOCATION[lang])
    captures = query.captures(root)
    return [get_node_name(source=source, node=capture[0], lang=lang) for capture in captures]


def extract_nl_from_code(source, root, lang, name=None, replace_method_name=False):
    """
    Extract nl tokens from given source code, including split name and method invocations.

    Args:
        source (str): Source code string
        root (tree_sitter.Node): Root of code
        lang (str): Source code language
        name (str): optional, name of method/function
        replace_method_name (bool): Whether to replace method name and returns a version that without names additionally

    Returns:
        Union[(str, str), str]:
            - Nl string
            - Nl string without method name

    """
    tokens = []
    tokens_wo_name = []

    if name is None:
        name = get_method_name(source=source, root=root, lang=lang)
    name_tokens = split_identifier(name)
    tokens += name_tokens

    invocations = extract_method_invocation(source=source, root=root, lang=lang)
    for invocation in invocations:
        subtokens = split_identifier(invocation)
        tokens += subtokens
        tokens_wo_name += subtokens

    if replace_method_name:
        return ' '.join(tokens), ' '.join(tokens_wo_name)
    else:
        return ' '.join(tokens)


def generate_single_ast_nl(source, lang, name=None, replace_method_name=False):
    """
    Generate AST sequence and nl sequence for a single source code sample.

    Args:
        source (str): Source code string
        lang (str): Source code language
        name (str): optional, name of method/function
        replace_method_name (bool): Whether to replace method name and returns a version that without names additionally

    Returns:
        Union[(str, str), (str, str, str)]:
            - AST sequence in string
            - Nl sequence in string

    """
    root = parse_ast(source=source, lang=lang)
    ast = generate_statement_xsbt(node=root, lang=lang)
    if replace_method_name:
        nl, nl_wo_name = extract_nl_from_code(source=source,
                                              root=root,
                                              lang=lang,
                                              name=name,
                                              replace_method_name=replace_method_name)
        return ast, nl, nl_wo_name
    else:
        nl = extract_nl_from_code(source=source, root=root, lang=lang, name=name)
        return ast, nl


def generate_asts_nls(sources, langs):
    """
    Generate AST sequence and nl sequence for a list of source code samples, exceptions will be eliminate.

    Args:
        sources (str): List of source code strings
        langs (str): List of source code languages

    Returns:
        (list[str], list[str], list[str], list[str]):
            - List of language strings
            - List of source code strings
            - List of AST sequence strings
            - List of nl sequence strings

    """
    assert len(sources) == len(langs)
    new_langs = []
    new_sources = []
    asts = []
    nls = []
    for lang, source in zip(langs, sources):
        try:
            ast, nl = generate_single_ast_nl(source=source, lang=lang)
            new_langs.append(lang)
            new_sources.append(source)
            asts.append(ast)
            nls.append(nl)
        except Exception:
            continue
    return new_langs, new_sources, asts, nls


# def get_ast_name(languages, code_lines):
#     assert len(languages) == len(code_lines)
#     langs = []
#     asts = []
#     names = []
#     codes = []
#     for lang, line in zip(languages, code_lines):
#         try:
#             tree = parse_ast(line, lang=lang)
#             ast = generate_statement_xsbt(line, tree.root_node)
#             name = get_method_name(line, lang=lang, root=tree.root_node)
#             langs.append(lang)
#             asts.append(' '.join(ast))
#             names.append(name)
#             codes.append(line)
#         except Exception:
#             continue
#     return langs, codes, asts, names
#
#
# def get_single_ast(lang, source):
#     tree = parse_ast(source=source, lang=lang)
#     ast = generate_statement_xsbt(tree.root_node)
#     return ' '.join(ast)
#
#
# def get_single_ast_name(lang, source):
#     tree = parse_ast(source=source, lang=lang)
#     ast = generate_statement_xsbt(tree.root_node)
#     name = get_method_name(source, lang=lang, root=tree.root_node)
#     return ast, name


# def lang_sample(lang):
#     import random, json
#     with open(f'../../../../dataset/pre_train/{lang}/valid/{lang}_valid_0.jsonl') as f:
#         line = f.readlines()[random.randint(0, 1000)]
#         data = json.loads(line.strip())
#         name = data['func_name']
#         source = data['code']
#     return source, name
#
#
# lang = 'java'
#
# source, name = lang_sample(lang)
# print('-' * 100)
# print('source:')
# print(source)
# print('-' * 100)
# print('name in json:')
# print(name)
# print('-' * 100)
#
# root = parse_ast(source, lang=lang)
# print('name extracted:')
# print(get_method_name(source=source, root=root, lang=lang))
# print('-' * 100)
# print('api sequence:')
# print(extract_method_invocation(source, root, lang))
# print('-' * 100)
# print('xsbt in statements:')
# print(generate_statement_xsbt(root, lang))
