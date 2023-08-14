# Implementation 1 of lexer using PyCParser
from pycparser.c_lexer import CLexer

# Implementation 2 of lexer/tokenizer using Tokompiler
#from ..tokompiler.lexicalization import lexicalize


# Not used so far
def error_func(self, msg, line, column):
  pass
def on_lbrace_func(self):
  pass
def on_rbrace_func(self):
  pass
def type_lookup_func(self, typ):
  pass

class PyCParser_CLexer(object):
    def __init__(self):
      self.clex = CLexer(error_func, lambda: None, lambda: None, lambda x: None)
      self.clex.build(optimize=False)

    def get_tokens(self, code):
      try:
        self.clex.input(code)
        tokens = []
        token = self.clex.token()
        while token != None:
          tokens.append(token.value)
          token = self.clex.token()
        return tokens
      except:
        return []

#class Tokompiler_CLexer(object):
#  def lexicalize(self, code):
#      return lexicalize(code, lang='c')
