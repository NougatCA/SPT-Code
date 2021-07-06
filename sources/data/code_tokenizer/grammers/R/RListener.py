# Generated from R.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RParser import RParser
else:
    from RParser import RParser

# This class defines a complete listener for a parse tree produced by RParser.
class RListener(ParseTreeListener):

    # Enter a parse tree produced by RParser#prog.
    def enterProg(self, ctx:RParser.ProgContext):
        pass

    # Exit a parse tree produced by RParser#prog.
    def exitProg(self, ctx:RParser.ProgContext):
        pass


    # Enter a parse tree produced by RParser#expr.
    def enterExpr(self, ctx:RParser.ExprContext):
        pass

    # Exit a parse tree produced by RParser#expr.
    def exitExpr(self, ctx:RParser.ExprContext):
        pass


    # Enter a parse tree produced by RParser#exprlist.
    def enterExprlist(self, ctx:RParser.ExprlistContext):
        pass

    # Exit a parse tree produced by RParser#exprlist.
    def exitExprlist(self, ctx:RParser.ExprlistContext):
        pass


    # Enter a parse tree produced by RParser#formlist.
    def enterFormlist(self, ctx:RParser.FormlistContext):
        pass

    # Exit a parse tree produced by RParser#formlist.
    def exitFormlist(self, ctx:RParser.FormlistContext):
        pass


    # Enter a parse tree produced by RParser#form.
    def enterForm(self, ctx:RParser.FormContext):
        pass

    # Exit a parse tree produced by RParser#form.
    def exitForm(self, ctx:RParser.FormContext):
        pass


    # Enter a parse tree produced by RParser#sublist.
    def enterSublist(self, ctx:RParser.SublistContext):
        pass

    # Exit a parse tree produced by RParser#sublist.
    def exitSublist(self, ctx:RParser.SublistContext):
        pass


    # Enter a parse tree produced by RParser#sub.
    def enterSub(self, ctx:RParser.SubContext):
        pass

    # Exit a parse tree produced by RParser#sub.
    def exitSub(self, ctx:RParser.SubContext):
        pass



del RParser