# Generated from GoParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GoParser import GoParser
else:
    from GoParser import GoParser

# This class defines a complete listener for a parse tree produced by GoParser.
class GoParserListener(ParseTreeListener):

    # Enter a parse tree produced by GoParser#sourceFile.
    def enterSourceFile(self, ctx:GoParser.SourceFileContext):
        pass

    # Exit a parse tree produced by GoParser#sourceFile.
    def exitSourceFile(self, ctx:GoParser.SourceFileContext):
        pass


    # Enter a parse tree produced by GoParser#packageClause.
    def enterPackageClause(self, ctx:GoParser.PackageClauseContext):
        pass

    # Exit a parse tree produced by GoParser#packageClause.
    def exitPackageClause(self, ctx:GoParser.PackageClauseContext):
        pass


    # Enter a parse tree produced by GoParser#importDecl.
    def enterImportDecl(self, ctx:GoParser.ImportDeclContext):
        pass

    # Exit a parse tree produced by GoParser#importDecl.
    def exitImportDecl(self, ctx:GoParser.ImportDeclContext):
        pass


    # Enter a parse tree produced by GoParser#importSpec.
    def enterImportSpec(self, ctx:GoParser.ImportSpecContext):
        pass

    # Exit a parse tree produced by GoParser#importSpec.
    def exitImportSpec(self, ctx:GoParser.ImportSpecContext):
        pass


    # Enter a parse tree produced by GoParser#importPath.
    def enterImportPath(self, ctx:GoParser.ImportPathContext):
        pass

    # Exit a parse tree produced by GoParser#importPath.
    def exitImportPath(self, ctx:GoParser.ImportPathContext):
        pass


    # Enter a parse tree produced by GoParser#declaration.
    def enterDeclaration(self, ctx:GoParser.DeclarationContext):
        pass

    # Exit a parse tree produced by GoParser#declaration.
    def exitDeclaration(self, ctx:GoParser.DeclarationContext):
        pass


    # Enter a parse tree produced by GoParser#constDecl.
    def enterConstDecl(self, ctx:GoParser.ConstDeclContext):
        pass

    # Exit a parse tree produced by GoParser#constDecl.
    def exitConstDecl(self, ctx:GoParser.ConstDeclContext):
        pass


    # Enter a parse tree produced by GoParser#constSpec.
    def enterConstSpec(self, ctx:GoParser.ConstSpecContext):
        pass

    # Exit a parse tree produced by GoParser#constSpec.
    def exitConstSpec(self, ctx:GoParser.ConstSpecContext):
        pass


    # Enter a parse tree produced by GoParser#identifierList.
    def enterIdentifierList(self, ctx:GoParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by GoParser#identifierList.
    def exitIdentifierList(self, ctx:GoParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by GoParser#expressionList.
    def enterExpressionList(self, ctx:GoParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by GoParser#expressionList.
    def exitExpressionList(self, ctx:GoParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by GoParser#typeDecl.
    def enterTypeDecl(self, ctx:GoParser.TypeDeclContext):
        pass

    # Exit a parse tree produced by GoParser#typeDecl.
    def exitTypeDecl(self, ctx:GoParser.TypeDeclContext):
        pass


    # Enter a parse tree produced by GoParser#typeSpec.
    def enterTypeSpec(self, ctx:GoParser.TypeSpecContext):
        pass

    # Exit a parse tree produced by GoParser#typeSpec.
    def exitTypeSpec(self, ctx:GoParser.TypeSpecContext):
        pass


    # Enter a parse tree produced by GoParser#functionDecl.
    def enterFunctionDecl(self, ctx:GoParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by GoParser#functionDecl.
    def exitFunctionDecl(self, ctx:GoParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by GoParser#methodDecl.
    def enterMethodDecl(self, ctx:GoParser.MethodDeclContext):
        pass

    # Exit a parse tree produced by GoParser#methodDecl.
    def exitMethodDecl(self, ctx:GoParser.MethodDeclContext):
        pass


    # Enter a parse tree produced by GoParser#receiver.
    def enterReceiver(self, ctx:GoParser.ReceiverContext):
        pass

    # Exit a parse tree produced by GoParser#receiver.
    def exitReceiver(self, ctx:GoParser.ReceiverContext):
        pass


    # Enter a parse tree produced by GoParser#varDecl.
    def enterVarDecl(self, ctx:GoParser.VarDeclContext):
        pass

    # Exit a parse tree produced by GoParser#varDecl.
    def exitVarDecl(self, ctx:GoParser.VarDeclContext):
        pass


    # Enter a parse tree produced by GoParser#varSpec.
    def enterVarSpec(self, ctx:GoParser.VarSpecContext):
        pass

    # Exit a parse tree produced by GoParser#varSpec.
    def exitVarSpec(self, ctx:GoParser.VarSpecContext):
        pass


    # Enter a parse tree produced by GoParser#block.
    def enterBlock(self, ctx:GoParser.BlockContext):
        pass

    # Exit a parse tree produced by GoParser#block.
    def exitBlock(self, ctx:GoParser.BlockContext):
        pass


    # Enter a parse tree produced by GoParser#statementList.
    def enterStatementList(self, ctx:GoParser.StatementListContext):
        pass

    # Exit a parse tree produced by GoParser#statementList.
    def exitStatementList(self, ctx:GoParser.StatementListContext):
        pass


    # Enter a parse tree produced by GoParser#statement.
    def enterStatement(self, ctx:GoParser.StatementContext):
        pass

    # Exit a parse tree produced by GoParser#statement.
    def exitStatement(self, ctx:GoParser.StatementContext):
        pass


    # Enter a parse tree produced by GoParser#simpleStmt.
    def enterSimpleStmt(self, ctx:GoParser.SimpleStmtContext):
        pass

    # Exit a parse tree produced by GoParser#simpleStmt.
    def exitSimpleStmt(self, ctx:GoParser.SimpleStmtContext):
        pass


    # Enter a parse tree produced by GoParser#expressionStmt.
    def enterExpressionStmt(self, ctx:GoParser.ExpressionStmtContext):
        pass

    # Exit a parse tree produced by GoParser#expressionStmt.
    def exitExpressionStmt(self, ctx:GoParser.ExpressionStmtContext):
        pass


    # Enter a parse tree produced by GoParser#sendStmt.
    def enterSendStmt(self, ctx:GoParser.SendStmtContext):
        pass

    # Exit a parse tree produced by GoParser#sendStmt.
    def exitSendStmt(self, ctx:GoParser.SendStmtContext):
        pass


    # Enter a parse tree produced by GoParser#incDecStmt.
    def enterIncDecStmt(self, ctx:GoParser.IncDecStmtContext):
        pass

    # Exit a parse tree produced by GoParser#incDecStmt.
    def exitIncDecStmt(self, ctx:GoParser.IncDecStmtContext):
        pass


    # Enter a parse tree produced by GoParser#assignment.
    def enterAssignment(self, ctx:GoParser.AssignmentContext):
        pass

    # Exit a parse tree produced by GoParser#assignment.
    def exitAssignment(self, ctx:GoParser.AssignmentContext):
        pass


    # Enter a parse tree produced by GoParser#assign_op.
    def enterAssign_op(self, ctx:GoParser.Assign_opContext):
        pass

    # Exit a parse tree produced by GoParser#assign_op.
    def exitAssign_op(self, ctx:GoParser.Assign_opContext):
        pass


    # Enter a parse tree produced by GoParser#shortVarDecl.
    def enterShortVarDecl(self, ctx:GoParser.ShortVarDeclContext):
        pass

    # Exit a parse tree produced by GoParser#shortVarDecl.
    def exitShortVarDecl(self, ctx:GoParser.ShortVarDeclContext):
        pass


    # Enter a parse tree produced by GoParser#emptyStmt.
    def enterEmptyStmt(self, ctx:GoParser.EmptyStmtContext):
        pass

    # Exit a parse tree produced by GoParser#emptyStmt.
    def exitEmptyStmt(self, ctx:GoParser.EmptyStmtContext):
        pass


    # Enter a parse tree produced by GoParser#labeledStmt.
    def enterLabeledStmt(self, ctx:GoParser.LabeledStmtContext):
        pass

    # Exit a parse tree produced by GoParser#labeledStmt.
    def exitLabeledStmt(self, ctx:GoParser.LabeledStmtContext):
        pass


    # Enter a parse tree produced by GoParser#returnStmt.
    def enterReturnStmt(self, ctx:GoParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by GoParser#returnStmt.
    def exitReturnStmt(self, ctx:GoParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by GoParser#breakStmt.
    def enterBreakStmt(self, ctx:GoParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by GoParser#breakStmt.
    def exitBreakStmt(self, ctx:GoParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by GoParser#continueStmt.
    def enterContinueStmt(self, ctx:GoParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by GoParser#continueStmt.
    def exitContinueStmt(self, ctx:GoParser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by GoParser#gotoStmt.
    def enterGotoStmt(self, ctx:GoParser.GotoStmtContext):
        pass

    # Exit a parse tree produced by GoParser#gotoStmt.
    def exitGotoStmt(self, ctx:GoParser.GotoStmtContext):
        pass


    # Enter a parse tree produced by GoParser#fallthroughStmt.
    def enterFallthroughStmt(self, ctx:GoParser.FallthroughStmtContext):
        pass

    # Exit a parse tree produced by GoParser#fallthroughStmt.
    def exitFallthroughStmt(self, ctx:GoParser.FallthroughStmtContext):
        pass


    # Enter a parse tree produced by GoParser#deferStmt.
    def enterDeferStmt(self, ctx:GoParser.DeferStmtContext):
        pass

    # Exit a parse tree produced by GoParser#deferStmt.
    def exitDeferStmt(self, ctx:GoParser.DeferStmtContext):
        pass


    # Enter a parse tree produced by GoParser#ifStmt.
    def enterIfStmt(self, ctx:GoParser.IfStmtContext):
        pass

    # Exit a parse tree produced by GoParser#ifStmt.
    def exitIfStmt(self, ctx:GoParser.IfStmtContext):
        pass


    # Enter a parse tree produced by GoParser#switchStmt.
    def enterSwitchStmt(self, ctx:GoParser.SwitchStmtContext):
        pass

    # Exit a parse tree produced by GoParser#switchStmt.
    def exitSwitchStmt(self, ctx:GoParser.SwitchStmtContext):
        pass


    # Enter a parse tree produced by GoParser#exprSwitchStmt.
    def enterExprSwitchStmt(self, ctx:GoParser.ExprSwitchStmtContext):
        pass

    # Exit a parse tree produced by GoParser#exprSwitchStmt.
    def exitExprSwitchStmt(self, ctx:GoParser.ExprSwitchStmtContext):
        pass


    # Enter a parse tree produced by GoParser#exprCaseClause.
    def enterExprCaseClause(self, ctx:GoParser.ExprCaseClauseContext):
        pass

    # Exit a parse tree produced by GoParser#exprCaseClause.
    def exitExprCaseClause(self, ctx:GoParser.ExprCaseClauseContext):
        pass


    # Enter a parse tree produced by GoParser#exprSwitchCase.
    def enterExprSwitchCase(self, ctx:GoParser.ExprSwitchCaseContext):
        pass

    # Exit a parse tree produced by GoParser#exprSwitchCase.
    def exitExprSwitchCase(self, ctx:GoParser.ExprSwitchCaseContext):
        pass


    # Enter a parse tree produced by GoParser#typeSwitchStmt.
    def enterTypeSwitchStmt(self, ctx:GoParser.TypeSwitchStmtContext):
        pass

    # Exit a parse tree produced by GoParser#typeSwitchStmt.
    def exitTypeSwitchStmt(self, ctx:GoParser.TypeSwitchStmtContext):
        pass


    # Enter a parse tree produced by GoParser#typeSwitchGuard.
    def enterTypeSwitchGuard(self, ctx:GoParser.TypeSwitchGuardContext):
        pass

    # Exit a parse tree produced by GoParser#typeSwitchGuard.
    def exitTypeSwitchGuard(self, ctx:GoParser.TypeSwitchGuardContext):
        pass


    # Enter a parse tree produced by GoParser#typeCaseClause.
    def enterTypeCaseClause(self, ctx:GoParser.TypeCaseClauseContext):
        pass

    # Exit a parse tree produced by GoParser#typeCaseClause.
    def exitTypeCaseClause(self, ctx:GoParser.TypeCaseClauseContext):
        pass


    # Enter a parse tree produced by GoParser#typeSwitchCase.
    def enterTypeSwitchCase(self, ctx:GoParser.TypeSwitchCaseContext):
        pass

    # Exit a parse tree produced by GoParser#typeSwitchCase.
    def exitTypeSwitchCase(self, ctx:GoParser.TypeSwitchCaseContext):
        pass


    # Enter a parse tree produced by GoParser#typeList.
    def enterTypeList(self, ctx:GoParser.TypeListContext):
        pass

    # Exit a parse tree produced by GoParser#typeList.
    def exitTypeList(self, ctx:GoParser.TypeListContext):
        pass


    # Enter a parse tree produced by GoParser#selectStmt.
    def enterSelectStmt(self, ctx:GoParser.SelectStmtContext):
        pass

    # Exit a parse tree produced by GoParser#selectStmt.
    def exitSelectStmt(self, ctx:GoParser.SelectStmtContext):
        pass


    # Enter a parse tree produced by GoParser#commClause.
    def enterCommClause(self, ctx:GoParser.CommClauseContext):
        pass

    # Exit a parse tree produced by GoParser#commClause.
    def exitCommClause(self, ctx:GoParser.CommClauseContext):
        pass


    # Enter a parse tree produced by GoParser#commCase.
    def enterCommCase(self, ctx:GoParser.CommCaseContext):
        pass

    # Exit a parse tree produced by GoParser#commCase.
    def exitCommCase(self, ctx:GoParser.CommCaseContext):
        pass


    # Enter a parse tree produced by GoParser#recvStmt.
    def enterRecvStmt(self, ctx:GoParser.RecvStmtContext):
        pass

    # Exit a parse tree produced by GoParser#recvStmt.
    def exitRecvStmt(self, ctx:GoParser.RecvStmtContext):
        pass


    # Enter a parse tree produced by GoParser#forStmt.
    def enterForStmt(self, ctx:GoParser.ForStmtContext):
        pass

    # Exit a parse tree produced by GoParser#forStmt.
    def exitForStmt(self, ctx:GoParser.ForStmtContext):
        pass


    # Enter a parse tree produced by GoParser#forClause.
    def enterForClause(self, ctx:GoParser.ForClauseContext):
        pass

    # Exit a parse tree produced by GoParser#forClause.
    def exitForClause(self, ctx:GoParser.ForClauseContext):
        pass


    # Enter a parse tree produced by GoParser#rangeClause.
    def enterRangeClause(self, ctx:GoParser.RangeClauseContext):
        pass

    # Exit a parse tree produced by GoParser#rangeClause.
    def exitRangeClause(self, ctx:GoParser.RangeClauseContext):
        pass


    # Enter a parse tree produced by GoParser#goStmt.
    def enterGoStmt(self, ctx:GoParser.GoStmtContext):
        pass

    # Exit a parse tree produced by GoParser#goStmt.
    def exitGoStmt(self, ctx:GoParser.GoStmtContext):
        pass


    # Enter a parse tree produced by GoParser#type_.
    def enterType_(self, ctx:GoParser.Type_Context):
        pass

    # Exit a parse tree produced by GoParser#type_.
    def exitType_(self, ctx:GoParser.Type_Context):
        pass


    # Enter a parse tree produced by GoParser#typeName.
    def enterTypeName(self, ctx:GoParser.TypeNameContext):
        pass

    # Exit a parse tree produced by GoParser#typeName.
    def exitTypeName(self, ctx:GoParser.TypeNameContext):
        pass


    # Enter a parse tree produced by GoParser#typeLit.
    def enterTypeLit(self, ctx:GoParser.TypeLitContext):
        pass

    # Exit a parse tree produced by GoParser#typeLit.
    def exitTypeLit(self, ctx:GoParser.TypeLitContext):
        pass


    # Enter a parse tree produced by GoParser#arrayType.
    def enterArrayType(self, ctx:GoParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by GoParser#arrayType.
    def exitArrayType(self, ctx:GoParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by GoParser#arrayLength.
    def enterArrayLength(self, ctx:GoParser.ArrayLengthContext):
        pass

    # Exit a parse tree produced by GoParser#arrayLength.
    def exitArrayLength(self, ctx:GoParser.ArrayLengthContext):
        pass


    # Enter a parse tree produced by GoParser#elementType.
    def enterElementType(self, ctx:GoParser.ElementTypeContext):
        pass

    # Exit a parse tree produced by GoParser#elementType.
    def exitElementType(self, ctx:GoParser.ElementTypeContext):
        pass


    # Enter a parse tree produced by GoParser#pointerType.
    def enterPointerType(self, ctx:GoParser.PointerTypeContext):
        pass

    # Exit a parse tree produced by GoParser#pointerType.
    def exitPointerType(self, ctx:GoParser.PointerTypeContext):
        pass


    # Enter a parse tree produced by GoParser#interfaceType.
    def enterInterfaceType(self, ctx:GoParser.InterfaceTypeContext):
        pass

    # Exit a parse tree produced by GoParser#interfaceType.
    def exitInterfaceType(self, ctx:GoParser.InterfaceTypeContext):
        pass


    # Enter a parse tree produced by GoParser#sliceType.
    def enterSliceType(self, ctx:GoParser.SliceTypeContext):
        pass

    # Exit a parse tree produced by GoParser#sliceType.
    def exitSliceType(self, ctx:GoParser.SliceTypeContext):
        pass


    # Enter a parse tree produced by GoParser#mapType.
    def enterMapType(self, ctx:GoParser.MapTypeContext):
        pass

    # Exit a parse tree produced by GoParser#mapType.
    def exitMapType(self, ctx:GoParser.MapTypeContext):
        pass


    # Enter a parse tree produced by GoParser#channelType.
    def enterChannelType(self, ctx:GoParser.ChannelTypeContext):
        pass

    # Exit a parse tree produced by GoParser#channelType.
    def exitChannelType(self, ctx:GoParser.ChannelTypeContext):
        pass


    # Enter a parse tree produced by GoParser#methodSpec.
    def enterMethodSpec(self, ctx:GoParser.MethodSpecContext):
        pass

    # Exit a parse tree produced by GoParser#methodSpec.
    def exitMethodSpec(self, ctx:GoParser.MethodSpecContext):
        pass


    # Enter a parse tree produced by GoParser#functionType.
    def enterFunctionType(self, ctx:GoParser.FunctionTypeContext):
        pass

    # Exit a parse tree produced by GoParser#functionType.
    def exitFunctionType(self, ctx:GoParser.FunctionTypeContext):
        pass


    # Enter a parse tree produced by GoParser#signature.
    def enterSignature(self, ctx:GoParser.SignatureContext):
        pass

    # Exit a parse tree produced by GoParser#signature.
    def exitSignature(self, ctx:GoParser.SignatureContext):
        pass


    # Enter a parse tree produced by GoParser#result.
    def enterResult(self, ctx:GoParser.ResultContext):
        pass

    # Exit a parse tree produced by GoParser#result.
    def exitResult(self, ctx:GoParser.ResultContext):
        pass


    # Enter a parse tree produced by GoParser#parameters.
    def enterParameters(self, ctx:GoParser.ParametersContext):
        pass

    # Exit a parse tree produced by GoParser#parameters.
    def exitParameters(self, ctx:GoParser.ParametersContext):
        pass


    # Enter a parse tree produced by GoParser#parameterDecl.
    def enterParameterDecl(self, ctx:GoParser.ParameterDeclContext):
        pass

    # Exit a parse tree produced by GoParser#parameterDecl.
    def exitParameterDecl(self, ctx:GoParser.ParameterDeclContext):
        pass


    # Enter a parse tree produced by GoParser#expression.
    def enterExpression(self, ctx:GoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by GoParser#expression.
    def exitExpression(self, ctx:GoParser.ExpressionContext):
        pass


    # Enter a parse tree produced by GoParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:GoParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by GoParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:GoParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by GoParser#unaryExpr.
    def enterUnaryExpr(self, ctx:GoParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by GoParser#unaryExpr.
    def exitUnaryExpr(self, ctx:GoParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by GoParser#conversion.
    def enterConversion(self, ctx:GoParser.ConversionContext):
        pass

    # Exit a parse tree produced by GoParser#conversion.
    def exitConversion(self, ctx:GoParser.ConversionContext):
        pass


    # Enter a parse tree produced by GoParser#operand.
    def enterOperand(self, ctx:GoParser.OperandContext):
        pass

    # Exit a parse tree produced by GoParser#operand.
    def exitOperand(self, ctx:GoParser.OperandContext):
        pass


    # Enter a parse tree produced by GoParser#literal.
    def enterLiteral(self, ctx:GoParser.LiteralContext):
        pass

    # Exit a parse tree produced by GoParser#literal.
    def exitLiteral(self, ctx:GoParser.LiteralContext):
        pass


    # Enter a parse tree produced by GoParser#basicLit.
    def enterBasicLit(self, ctx:GoParser.BasicLitContext):
        pass

    # Exit a parse tree produced by GoParser#basicLit.
    def exitBasicLit(self, ctx:GoParser.BasicLitContext):
        pass


    # Enter a parse tree produced by GoParser#integer.
    def enterInteger(self, ctx:GoParser.IntegerContext):
        pass

    # Exit a parse tree produced by GoParser#integer.
    def exitInteger(self, ctx:GoParser.IntegerContext):
        pass


    # Enter a parse tree produced by GoParser#operandName.
    def enterOperandName(self, ctx:GoParser.OperandNameContext):
        pass

    # Exit a parse tree produced by GoParser#operandName.
    def exitOperandName(self, ctx:GoParser.OperandNameContext):
        pass


    # Enter a parse tree produced by GoParser#qualifiedIdent.
    def enterQualifiedIdent(self, ctx:GoParser.QualifiedIdentContext):
        pass

    # Exit a parse tree produced by GoParser#qualifiedIdent.
    def exitQualifiedIdent(self, ctx:GoParser.QualifiedIdentContext):
        pass


    # Enter a parse tree produced by GoParser#compositeLit.
    def enterCompositeLit(self, ctx:GoParser.CompositeLitContext):
        pass

    # Exit a parse tree produced by GoParser#compositeLit.
    def exitCompositeLit(self, ctx:GoParser.CompositeLitContext):
        pass


    # Enter a parse tree produced by GoParser#literalType.
    def enterLiteralType(self, ctx:GoParser.LiteralTypeContext):
        pass

    # Exit a parse tree produced by GoParser#literalType.
    def exitLiteralType(self, ctx:GoParser.LiteralTypeContext):
        pass


    # Enter a parse tree produced by GoParser#literalValue.
    def enterLiteralValue(self, ctx:GoParser.LiteralValueContext):
        pass

    # Exit a parse tree produced by GoParser#literalValue.
    def exitLiteralValue(self, ctx:GoParser.LiteralValueContext):
        pass


    # Enter a parse tree produced by GoParser#elementList.
    def enterElementList(self, ctx:GoParser.ElementListContext):
        pass

    # Exit a parse tree produced by GoParser#elementList.
    def exitElementList(self, ctx:GoParser.ElementListContext):
        pass


    # Enter a parse tree produced by GoParser#keyedElement.
    def enterKeyedElement(self, ctx:GoParser.KeyedElementContext):
        pass

    # Exit a parse tree produced by GoParser#keyedElement.
    def exitKeyedElement(self, ctx:GoParser.KeyedElementContext):
        pass


    # Enter a parse tree produced by GoParser#key.
    def enterKey(self, ctx:GoParser.KeyContext):
        pass

    # Exit a parse tree produced by GoParser#key.
    def exitKey(self, ctx:GoParser.KeyContext):
        pass


    # Enter a parse tree produced by GoParser#element.
    def enterElement(self, ctx:GoParser.ElementContext):
        pass

    # Exit a parse tree produced by GoParser#element.
    def exitElement(self, ctx:GoParser.ElementContext):
        pass


    # Enter a parse tree produced by GoParser#structType.
    def enterStructType(self, ctx:GoParser.StructTypeContext):
        pass

    # Exit a parse tree produced by GoParser#structType.
    def exitStructType(self, ctx:GoParser.StructTypeContext):
        pass


    # Enter a parse tree produced by GoParser#fieldDecl.
    def enterFieldDecl(self, ctx:GoParser.FieldDeclContext):
        pass

    # Exit a parse tree produced by GoParser#fieldDecl.
    def exitFieldDecl(self, ctx:GoParser.FieldDeclContext):
        pass


    # Enter a parse tree produced by GoParser#string_.
    def enterString_(self, ctx:GoParser.String_Context):
        pass

    # Exit a parse tree produced by GoParser#string_.
    def exitString_(self, ctx:GoParser.String_Context):
        pass


    # Enter a parse tree produced by GoParser#embeddedField.
    def enterEmbeddedField(self, ctx:GoParser.EmbeddedFieldContext):
        pass

    # Exit a parse tree produced by GoParser#embeddedField.
    def exitEmbeddedField(self, ctx:GoParser.EmbeddedFieldContext):
        pass


    # Enter a parse tree produced by GoParser#functionLit.
    def enterFunctionLit(self, ctx:GoParser.FunctionLitContext):
        pass

    # Exit a parse tree produced by GoParser#functionLit.
    def exitFunctionLit(self, ctx:GoParser.FunctionLitContext):
        pass


    # Enter a parse tree produced by GoParser#index.
    def enterIndex(self, ctx:GoParser.IndexContext):
        pass

    # Exit a parse tree produced by GoParser#index.
    def exitIndex(self, ctx:GoParser.IndexContext):
        pass


    # Enter a parse tree produced by GoParser#slice_.
    def enterSlice_(self, ctx:GoParser.Slice_Context):
        pass

    # Exit a parse tree produced by GoParser#slice_.
    def exitSlice_(self, ctx:GoParser.Slice_Context):
        pass


    # Enter a parse tree produced by GoParser#typeAssertion.
    def enterTypeAssertion(self, ctx:GoParser.TypeAssertionContext):
        pass

    # Exit a parse tree produced by GoParser#typeAssertion.
    def exitTypeAssertion(self, ctx:GoParser.TypeAssertionContext):
        pass


    # Enter a parse tree produced by GoParser#arguments.
    def enterArguments(self, ctx:GoParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by GoParser#arguments.
    def exitArguments(self, ctx:GoParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by GoParser#methodExpr.
    def enterMethodExpr(self, ctx:GoParser.MethodExprContext):
        pass

    # Exit a parse tree produced by GoParser#methodExpr.
    def exitMethodExpr(self, ctx:GoParser.MethodExprContext):
        pass


    # Enter a parse tree produced by GoParser#receiverType.
    def enterReceiverType(self, ctx:GoParser.ReceiverTypeContext):
        pass

    # Exit a parse tree produced by GoParser#receiverType.
    def exitReceiverType(self, ctx:GoParser.ReceiverTypeContext):
        pass


    # Enter a parse tree produced by GoParser#eos.
    def enterEos(self, ctx:GoParser.EosContext):
        pass

    # Exit a parse tree produced by GoParser#eos.
    def exitEos(self, ctx:GoParser.EosContext):
        pass



del GoParser