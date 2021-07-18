
class Indenter(object):

    def __init__(self):
        self.indent_string = ''
        self.indent_size = 2

    def get_indent_string(self):
        return self.indent_string

    def set_indent_size(self, indent_size):
        self.indent_size = indent_size

    def indent(self):
        self.indent_string += ' ' * self.indent_size

    def unindent(self):
        if len(self.indent_string) < self.indent_size:
            self.indent_string = ''
        else:
            self.indent_string -= ' ' * self.indent_size
