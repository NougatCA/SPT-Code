
from tree_sitter import Language

import subprocess
import os

# for lang in ['go', 'javascript', 'python', 'java', 'php', 'ruby', 'c-sharp']:
#     subprocess.run(['git', 'clone', f'git@github.com:tree-sitter/tree-sitter-{lang}.git',
#                     f'vendor/tree-sitter-{lang}'])

Language.build_library(
    # Store the library in the `build` directory
    'build/my-languages.so',

    # Include one or more languages
    [
        'vendor/tree-sitter-go',
        'vendor/tree-sitter-javascript',
        'vendor/tree-sitter-python',
        'vendor/tree-sitter-java',
        'vendor/tree-sitter-php',
        'vendor/tree-sitter-ruby',
        'vendor/tree-sitter-c-sharp'
    ]
)
