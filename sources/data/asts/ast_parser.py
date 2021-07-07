import tree_sitter
from tree_sitter import Language, Parser
import os


LANGUAGE = {'go': Language('build/my-languages.so', 'go'),
            'javascript': Language('build/my-languages.so', 'javascript'),
            'python': Language('build/my-languages.so', 'python'),
            'java': Language('build/my-languages.so', 'java'),
            'php': Language('build/my-languages.so', 'php'),
            'ruby': Language('build/my-languages.so', 'ruby'),
            'c-sharp': Language('build/my-languages.so', 'c_sharp')}
parser = Parser()

method_name_query_string = """
(program
  (local_variable_declaration
    (variable_declarator
      (identifier) @method_name)))
"""

method_invocation_query_string = """
(method_invocation
  [
    (
        (*)
        .
        (identifier) @method_invocation
    )
    
    (
        (identifier) @method_invocation
    )
  ]
)
"""

ELIMINATE_AST_NODE = ['(', ')', '{', '}', ';']


def parse_ast(code, language=None):
    """
    Parse the given code into corresponding ast.
    Args:
        code (str): code in string
        language (str): Optional, if given, set the language

    Returns:
        tree_sitter.Tree: parsed ast tree, not root node, get root by ``tree.root_node''

    """
    if language:
        parser.set_language(LANGUAGE[language])
    tree = parser.parse(str.encode(code))
    return tree


def get_paths(root: tree_sitter.Node):

    node_stack = []
    path_stack = []
    result = []

    node_stack.append(root)
    init_path = [root]
    path_stack.append(init_path)

    while node_stack:
        cur_node = node_stack.pop()
        cur_path = path_stack.pop()

        if len(cur_node.children) <= 0:
            result.append(cur_path)

        else:
            num_children = len(cur_node.children)
            for i in range(num_children - 1, -1, -1):
                child = cur_node.children[i]
                node_stack.append(child)
                new_path = cur_path[:]
                new_path.append(child)
                path_stack.append(new_path)

    return result


def get_node_name(source, node):
    if node.is_named:
        return source[node.start_byte: node.end_byte]
    return ''


def get_method_name(source, language, node):
    if node.type != 'program':
        return ''
    query = LANGUAGE[language].query(method_name_query_string)
    captures = query.captures(node)
    return get_node_name(source, captures[0][0])


def get_xsbt(source, node):
    xsbt = []
    if len(node.children) == 0:
        if get_node_name(source, node) not in ELIMINATE_AST_NODE and \
           node.type not in ELIMINATE_AST_NODE:
            xsbt.append(node.type)
    else:
        xsbt.append(f'<{node.type}>')
        len_before = len(xsbt)
        for child in node.children:
            xsbt += get_xsbt(source, child)
        if len_before == len(xsbt) and len_before != 0:
            xsbt[-1] = node.type
        else:
            xsbt.append(f'</{node.type}>')
    return xsbt


def get_statement_xsbt(node):
    xsbt = []

    if len(node.children) == 0:
        if node.type.endswith('statement'):
            xsbt.append(node.type)
    else:
        if node.type.endswith('statement'):
            xsbt.append(f'<{node.type}>')
        len_before = len(xsbt)
        for child in node.children:
            xsbt += get_statement_xsbt(child)
        if len_before == len(xsbt) and len_before != 0:
            xsbt[-1] = node.type
        elif node.type.endswith('statement'):
            xsbt.append(f'</{node.type}>')

    return xsbt


def get_ast_name(languages, code_lines):
    # TODO: add api sequence as nl
    assert len(languages) == len(code_lines)
    langs = []
    asts = []
    names = []
    codes = []
    for lang, line in zip(languages, code_lines):
        try:
            tree = parse_ast(line, language=lang)
            ast = get_xsbt(line, tree.root_node)
            name = get_method_name(line, language=lang, node=tree.root_node)
            langs.append(lang)
            asts.append(' '.join(ast))
            names.append(name)
            codes.append(line)
        except Exception:
            continue
    return langs, codes, asts, names


def get_single_ast(language, source):
    tree = parse_ast(code=source, language=language)
    # ast = get_xsbt(source=source, node=tree.root_node)
    ast = get_statement_xsbt(tree.root_node)
    return ' '.join(ast)


def get_single_ast_name(language, source):
    tree = parse_ast(code=source, language=language)
    ast = get_statement_xsbt(tree.root_node)
    name = get_method_name(source, language=language, node=tree.root_node)
    return ast, name


def get_method_invocation(root, source, lang):
    query = LANGUAGE[lang].query(method_invocation_query_string)
    captures = query.captures(root)
    return [get_node_name(source=source, node=capture[0]) for capture in captures]


source = '@CanIgnoreReturnValue\n  public static <T> boolean removeIf(Iterator<T> removeFrom, Predicate<? super T> predicate) {\n    checkNotNull(predicate);\n    boolean modified = false;\n    while (removeFrom.hasNext()) {\n      if (predicate.apply(removeFrom.next())) {\n        removeFrom.remove();\n        modified = true;\n      }\n    }\n    return modified;\n  }'
tree = parse_ast(source, language='java')

paths = get_paths(tree.root_node)
for path in paths:
    print(' '.join([node.type for node in path] + [get_node_name(source, path[-1])]))

print(get_method_name(source, language='java', node=tree.root_node))
print(get_method_invocation(tree.root_node, source, 'java'))
