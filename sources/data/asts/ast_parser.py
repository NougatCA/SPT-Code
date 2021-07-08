import random
import json

import tree_sitter
from tree_sitter import Language, Parser
from ..data_utils import split_identifier

import vars


LANGUAGE = {vars.GO_LANG: Language('build/my-languages.so', 'go'),
            vars.JAVASCRIPT_LANG: Language('build/my-languages.so', 'javascript'),
            vars.PYTHON_LANG: Language('build/my-languages.so', 'python'),
            vars.JAVA_LANG: Language('build/my-languages.so', 'java'),
            vars.PHP_LANG: Language('build/my-languages.so', 'php'),
            vars.RUBY_LANG: Language('build/my-languages.so', 'ruby'),
            vars.C_SHARP_LANG: Language('build/my-languages.so', 'c_sharp')}

parser = Parser()

PHP_SOURCE_PREFIX = '<?php '
PHP_SOURCE_POSTFIX = ' ?>'

PATTERNS_METHOD_NAME = {
    vars.JAVA_LANG: """
    (program
        (local_variable_declaration
            declarator: (variable_declarator
                name: (identifier) @method_name)
        )
    )
    """,

    vars.PYTHON_LANG: """
    (module
        (function_definition
            name: (identifier) @method_name
        )
    )
    """,

    vars.GO_LANG: """
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

    vars.JAVASCRIPT_LANG: """
    (program
        (function_declaration
            name: (identifier) @method_name
        )
    )
    """,

    vars.RUBY_LANG: """
    (program
        (method
            name: (identifier) @method_name
        )
    )
    """,

    vars.PHP_LANG: """
    (program
        (function_definition
            name: (name) @method_name
        )
    )
    """
}

PATTERNS_METHOD_INVOCATION = {
    vars.JAVA_LANG: """
    (method_invocation
        name: (identifier) @method_invocation
    )
    """,

    vars.PYTHON_LANG: """
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

    vars.GO_LANG: """
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

    vars.JAVASCRIPT_LANG: """
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

    vars.RUBY_LANG: """
    (call
        method: (identifier) @method_invocation
    )
    """,

    vars.PHP_LANG: """
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

ENDING_STRINGS_STATEMENT = {
    vars.JAVA_LANG: 'statement',
    vars.PYTHON_LANG: 'statement',
    vars.GO_LANG: 'statement',
    vars.JAVASCRIPT_LANG: 'statement',
    vars.RUBY_LANG: ['call', 'assignment', 'if', 'unless_modifier', 'operator_assignment', 'if_modifier', 'return',
                     'rescue', 'else', 'unless', 'when', 'for', 'while_modifier', 'until'],
    vars.PHP_LANG: 'statement'
}


ELIMINATE_AST_NODE = ['(', ')', '{', '}', ';']


def parse_ast(source, lang):
    """
    Parse the given code into corresponding ast.
    Args:
        source (str): code in string
        lang (str): Set the language

    Returns:
        tree_sitter.Tree: parsed ast tree, not root node, get root by ``tree.root_node''

    """
    parser.set_language(LANGUAGE[lang])
    if lang == vars.PHP_LANG:
        source = PHP_SOURCE_PREFIX + source + PHP_SOURCE_POSTFIX
    tree = parser.parse(str.encode(source))
    return tree


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
        if lang == vars.PHP_LANG:
            return source[node.start_byte - len(PHP_SOURCE_PREFIX): node.end_byte - len(PHP_SOURCE_PREFIX)]
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
    ending = ENDING_STRINGS_STATEMENT[lang]
    if isinstance(ending, str):
        return node.type.endswith(ending)
    else:
        for end in ending:
            if node.type.endswith(end):
                return True
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
    return f'{node.type}_statement' if lang == vars.RUBY_LANG else node.type


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
            xsbt.append(f'<{get_node_type(node, lang)}>')
        len_before = len(xsbt)
        for child in node.children:
            xsbt += __statement_xsbt(node=child, lang=lang)
        if len_before == len(xsbt) and len_before != 0:
            xsbt[-1] = get_node_type(node, lang)
        elif is_statement_node(node, lang):
            xsbt.append(f'</{get_node_type(node, lang)}>')

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


def extract_nl_from_code(source, root, lang, name=None):
    """
    Extract nl tokens from given source code, including split name and method invocations.

    Args:
        source (str): Source code string
        root (tree_sitter.Node): Root of code
        lang (str): Source code language
        name (str): optional, name of method/function

    Returns:
        str: Nl string

    """
    tokens = []

    if name is None:
        name = get_method_name(source=source, root=root, lang=lang)
    name_tokens = split_identifier(name)
    tokens += name_tokens

    invocations = extract_method_invocation(source=source, root=root, lang=lang)
    for invocation in invocations:
        subtokens = split_identifier(invocation)
        tokens += subtokens

    return ' '.join(tokens)


def generate_single_ast_nl(source, lang, name=None):
    """
    Generate AST sequence and nl sequence for a single source code sample.

    Args:
        source (str): Source code string
        lang (str): Source code language
        name (str): optional, name of method/function

    Returns:
        (str, str):
            - AST sequence in string
            - Nl sequence in string

    """
    tree = parse_ast(source=source, lang=lang)
    ast = generate_statement_xsbt(node=tree.root_node, lang=lang)
    nl = extract_nl_from_code(source=source, root=tree.root_node, lang=lang, name=name)
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
#     with open(f'../../../../dataset/pre_train/{lang}/valid/{lang}_valid_0.jsonl') as f:
#         line = f.readlines()[random.randint(0, 1000)]
#         data = json.loads(line.strip())
#         name = data['func_name']
#         source = data['code']
#         code = ' '.join(data['code_tokens'])
#     return source, code, name
#
#
# lang = 'php'
#
# source, code, name = lang_sample(lang)
# print('-' * 100)
# print('source:')
# print(source)
# print('-' * 100)
# print('code')
# print(code)
# print('-' * 100)
# print('name in json:')
# print(name)
# print('-' * 100)
#
# tree = parse_ast(source, lang=lang)
# print('name extracted:')
# print(get_method_name(source=source, root=tree.root_node, lang=lang))
# print('-' * 100)
# print('api sequence:')
# print(extract_method_invocation(source, tree.root_node, lang))
# print('-' * 100)
# print('xsbt in statements:')
# print(' '.join(generate_statement_xsbt(tree.root_node, lang)))
