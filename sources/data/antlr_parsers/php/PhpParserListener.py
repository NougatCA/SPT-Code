# Generated from PhpParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PhpParser import PhpParser
else:
    from PhpParser import PhpParser

# This class defines a complete listener for a parse tree produced by PhpParser.
class PhpParserListener(ParseTreeListener):

    # Enter a parse tree produced by PhpParser#htmlDocument.
    def enterHtmlDocument(self, ctx:PhpParser.HtmlDocumentContext):
        pass

    # Exit a parse tree produced by PhpParser#htmlDocument.
    def exitHtmlDocument(self, ctx:PhpParser.HtmlDocumentContext):
        pass


    # Enter a parse tree produced by PhpParser#inlineHtml.
    def enterInlineHtml(self, ctx:PhpParser.InlineHtmlContext):
        pass

    # Exit a parse tree produced by PhpParser#inlineHtml.
    def exitInlineHtml(self, ctx:PhpParser.InlineHtmlContext):
        pass


    # Enter a parse tree produced by PhpParser#htmlElement.
    def enterHtmlElement(self, ctx:PhpParser.HtmlElementContext):
        pass

    # Exit a parse tree produced by PhpParser#htmlElement.
    def exitHtmlElement(self, ctx:PhpParser.HtmlElementContext):
        pass


    # Enter a parse tree produced by PhpParser#scriptText.
    def enterScriptText(self, ctx:PhpParser.ScriptTextContext):
        pass

    # Exit a parse tree produced by PhpParser#scriptText.
    def exitScriptText(self, ctx:PhpParser.ScriptTextContext):
        pass


    # Enter a parse tree produced by PhpParser#phpBlock.
    def enterPhpBlock(self, ctx:PhpParser.PhpBlockContext):
        pass

    # Exit a parse tree produced by PhpParser#phpBlock.
    def exitPhpBlock(self, ctx:PhpParser.PhpBlockContext):
        pass


    # Enter a parse tree produced by PhpParser#importStatement.
    def enterImportStatement(self, ctx:PhpParser.ImportStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#importStatement.
    def exitImportStatement(self, ctx:PhpParser.ImportStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#topStatement.
    def enterTopStatement(self, ctx:PhpParser.TopStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#topStatement.
    def exitTopStatement(self, ctx:PhpParser.TopStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#useDeclaration.
    def enterUseDeclaration(self, ctx:PhpParser.UseDeclarationContext):
        pass

    # Exit a parse tree produced by PhpParser#useDeclaration.
    def exitUseDeclaration(self, ctx:PhpParser.UseDeclarationContext):
        pass


    # Enter a parse tree produced by PhpParser#useDeclarationContentList.
    def enterUseDeclarationContentList(self, ctx:PhpParser.UseDeclarationContentListContext):
        pass

    # Exit a parse tree produced by PhpParser#useDeclarationContentList.
    def exitUseDeclarationContentList(self, ctx:PhpParser.UseDeclarationContentListContext):
        pass


    # Enter a parse tree produced by PhpParser#useDeclarationContent.
    def enterUseDeclarationContent(self, ctx:PhpParser.UseDeclarationContentContext):
        pass

    # Exit a parse tree produced by PhpParser#useDeclarationContent.
    def exitUseDeclarationContent(self, ctx:PhpParser.UseDeclarationContentContext):
        pass


    # Enter a parse tree produced by PhpParser#namespaceDeclaration.
    def enterNamespaceDeclaration(self, ctx:PhpParser.NamespaceDeclarationContext):
        pass

    # Exit a parse tree produced by PhpParser#namespaceDeclaration.
    def exitNamespaceDeclaration(self, ctx:PhpParser.NamespaceDeclarationContext):
        pass


    # Enter a parse tree produced by PhpParser#namespaceStatement.
    def enterNamespaceStatement(self, ctx:PhpParser.NamespaceStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#namespaceStatement.
    def exitNamespaceStatement(self, ctx:PhpParser.NamespaceStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:PhpParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by PhpParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:PhpParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by PhpParser#classDeclaration.
    def enterClassDeclaration(self, ctx:PhpParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by PhpParser#classDeclaration.
    def exitClassDeclaration(self, ctx:PhpParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by PhpParser#classEntryType.
    def enterClassEntryType(self, ctx:PhpParser.ClassEntryTypeContext):
        pass

    # Exit a parse tree produced by PhpParser#classEntryType.
    def exitClassEntryType(self, ctx:PhpParser.ClassEntryTypeContext):
        pass


    # Enter a parse tree produced by PhpParser#interfaceList.
    def enterInterfaceList(self, ctx:PhpParser.InterfaceListContext):
        pass

    # Exit a parse tree produced by PhpParser#interfaceList.
    def exitInterfaceList(self, ctx:PhpParser.InterfaceListContext):
        pass


    # Enter a parse tree produced by PhpParser#typeParameterListInBrackets.
    def enterTypeParameterListInBrackets(self, ctx:PhpParser.TypeParameterListInBracketsContext):
        pass

    # Exit a parse tree produced by PhpParser#typeParameterListInBrackets.
    def exitTypeParameterListInBrackets(self, ctx:PhpParser.TypeParameterListInBracketsContext):
        pass


    # Enter a parse tree produced by PhpParser#typeParameterList.
    def enterTypeParameterList(self, ctx:PhpParser.TypeParameterListContext):
        pass

    # Exit a parse tree produced by PhpParser#typeParameterList.
    def exitTypeParameterList(self, ctx:PhpParser.TypeParameterListContext):
        pass


    # Enter a parse tree produced by PhpParser#typeParameterWithDefaultsList.
    def enterTypeParameterWithDefaultsList(self, ctx:PhpParser.TypeParameterWithDefaultsListContext):
        pass

    # Exit a parse tree produced by PhpParser#typeParameterWithDefaultsList.
    def exitTypeParameterWithDefaultsList(self, ctx:PhpParser.TypeParameterWithDefaultsListContext):
        pass


    # Enter a parse tree produced by PhpParser#typeParameterDecl.
    def enterTypeParameterDecl(self, ctx:PhpParser.TypeParameterDeclContext):
        pass

    # Exit a parse tree produced by PhpParser#typeParameterDecl.
    def exitTypeParameterDecl(self, ctx:PhpParser.TypeParameterDeclContext):
        pass


    # Enter a parse tree produced by PhpParser#typeParameterWithDefaultDecl.
    def enterTypeParameterWithDefaultDecl(self, ctx:PhpParser.TypeParameterWithDefaultDeclContext):
        pass

    # Exit a parse tree produced by PhpParser#typeParameterWithDefaultDecl.
    def exitTypeParameterWithDefaultDecl(self, ctx:PhpParser.TypeParameterWithDefaultDeclContext):
        pass


    # Enter a parse tree produced by PhpParser#genericDynamicArgs.
    def enterGenericDynamicArgs(self, ctx:PhpParser.GenericDynamicArgsContext):
        pass

    # Exit a parse tree produced by PhpParser#genericDynamicArgs.
    def exitGenericDynamicArgs(self, ctx:PhpParser.GenericDynamicArgsContext):
        pass


    # Enter a parse tree produced by PhpParser#attributes.
    def enterAttributes(self, ctx:PhpParser.AttributesContext):
        pass

    # Exit a parse tree produced by PhpParser#attributes.
    def exitAttributes(self, ctx:PhpParser.AttributesContext):
        pass


    # Enter a parse tree produced by PhpParser#attributeGroup.
    def enterAttributeGroup(self, ctx:PhpParser.AttributeGroupContext):
        pass

    # Exit a parse tree produced by PhpParser#attributeGroup.
    def exitAttributeGroup(self, ctx:PhpParser.AttributeGroupContext):
        pass


    # Enter a parse tree produced by PhpParser#attribute.
    def enterAttribute(self, ctx:PhpParser.AttributeContext):
        pass

    # Exit a parse tree produced by PhpParser#attribute.
    def exitAttribute(self, ctx:PhpParser.AttributeContext):
        pass


    # Enter a parse tree produced by PhpParser#innerStatementList.
    def enterInnerStatementList(self, ctx:PhpParser.InnerStatementListContext):
        pass

    # Exit a parse tree produced by PhpParser#innerStatementList.
    def exitInnerStatementList(self, ctx:PhpParser.InnerStatementListContext):
        pass


    # Enter a parse tree produced by PhpParser#innerStatement.
    def enterInnerStatement(self, ctx:PhpParser.InnerStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#innerStatement.
    def exitInnerStatement(self, ctx:PhpParser.InnerStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#statement.
    def enterStatement(self, ctx:PhpParser.StatementContext):
        pass

    # Exit a parse tree produced by PhpParser#statement.
    def exitStatement(self, ctx:PhpParser.StatementContext):
        pass


    # Enter a parse tree produced by PhpParser#emptyStatement.
    def enterEmptyStatement(self, ctx:PhpParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#emptyStatement.
    def exitEmptyStatement(self, ctx:PhpParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#blockStatement.
    def enterBlockStatement(self, ctx:PhpParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#blockStatement.
    def exitBlockStatement(self, ctx:PhpParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#ifStatement.
    def enterIfStatement(self, ctx:PhpParser.IfStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#ifStatement.
    def exitIfStatement(self, ctx:PhpParser.IfStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#elseIfStatement.
    def enterElseIfStatement(self, ctx:PhpParser.ElseIfStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#elseIfStatement.
    def exitElseIfStatement(self, ctx:PhpParser.ElseIfStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#elseIfColonStatement.
    def enterElseIfColonStatement(self, ctx:PhpParser.ElseIfColonStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#elseIfColonStatement.
    def exitElseIfColonStatement(self, ctx:PhpParser.ElseIfColonStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#elseStatement.
    def enterElseStatement(self, ctx:PhpParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#elseStatement.
    def exitElseStatement(self, ctx:PhpParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#elseColonStatement.
    def enterElseColonStatement(self, ctx:PhpParser.ElseColonStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#elseColonStatement.
    def exitElseColonStatement(self, ctx:PhpParser.ElseColonStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#whileStatement.
    def enterWhileStatement(self, ctx:PhpParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#whileStatement.
    def exitWhileStatement(self, ctx:PhpParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:PhpParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:PhpParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#forStatement.
    def enterForStatement(self, ctx:PhpParser.ForStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#forStatement.
    def exitForStatement(self, ctx:PhpParser.ForStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#forInit.
    def enterForInit(self, ctx:PhpParser.ForInitContext):
        pass

    # Exit a parse tree produced by PhpParser#forInit.
    def exitForInit(self, ctx:PhpParser.ForInitContext):
        pass


    # Enter a parse tree produced by PhpParser#forUpdate.
    def enterForUpdate(self, ctx:PhpParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by PhpParser#forUpdate.
    def exitForUpdate(self, ctx:PhpParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by PhpParser#switchStatement.
    def enterSwitchStatement(self, ctx:PhpParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#switchStatement.
    def exitSwitchStatement(self, ctx:PhpParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#switchBlock.
    def enterSwitchBlock(self, ctx:PhpParser.SwitchBlockContext):
        pass

    # Exit a parse tree produced by PhpParser#switchBlock.
    def exitSwitchBlock(self, ctx:PhpParser.SwitchBlockContext):
        pass


    # Enter a parse tree produced by PhpParser#breakStatement.
    def enterBreakStatement(self, ctx:PhpParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#breakStatement.
    def exitBreakStatement(self, ctx:PhpParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#continueStatement.
    def enterContinueStatement(self, ctx:PhpParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#continueStatement.
    def exitContinueStatement(self, ctx:PhpParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#returnStatement.
    def enterReturnStatement(self, ctx:PhpParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#returnStatement.
    def exitReturnStatement(self, ctx:PhpParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#expressionStatement.
    def enterExpressionStatement(self, ctx:PhpParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#expressionStatement.
    def exitExpressionStatement(self, ctx:PhpParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#unsetStatement.
    def enterUnsetStatement(self, ctx:PhpParser.UnsetStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#unsetStatement.
    def exitUnsetStatement(self, ctx:PhpParser.UnsetStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#foreachStatement.
    def enterForeachStatement(self, ctx:PhpParser.ForeachStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#foreachStatement.
    def exitForeachStatement(self, ctx:PhpParser.ForeachStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#tryCatchFinally.
    def enterTryCatchFinally(self, ctx:PhpParser.TryCatchFinallyContext):
        pass

    # Exit a parse tree produced by PhpParser#tryCatchFinally.
    def exitTryCatchFinally(self, ctx:PhpParser.TryCatchFinallyContext):
        pass


    # Enter a parse tree produced by PhpParser#catchClause.
    def enterCatchClause(self, ctx:PhpParser.CatchClauseContext):
        pass

    # Exit a parse tree produced by PhpParser#catchClause.
    def exitCatchClause(self, ctx:PhpParser.CatchClauseContext):
        pass


    # Enter a parse tree produced by PhpParser#finallyStatement.
    def enterFinallyStatement(self, ctx:PhpParser.FinallyStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#finallyStatement.
    def exitFinallyStatement(self, ctx:PhpParser.FinallyStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#throwStatement.
    def enterThrowStatement(self, ctx:PhpParser.ThrowStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#throwStatement.
    def exitThrowStatement(self, ctx:PhpParser.ThrowStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#gotoStatement.
    def enterGotoStatement(self, ctx:PhpParser.GotoStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#gotoStatement.
    def exitGotoStatement(self, ctx:PhpParser.GotoStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#declareStatement.
    def enterDeclareStatement(self, ctx:PhpParser.DeclareStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#declareStatement.
    def exitDeclareStatement(self, ctx:PhpParser.DeclareStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#inlineHtmlStatement.
    def enterInlineHtmlStatement(self, ctx:PhpParser.InlineHtmlStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#inlineHtmlStatement.
    def exitInlineHtmlStatement(self, ctx:PhpParser.InlineHtmlStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#declareList.
    def enterDeclareList(self, ctx:PhpParser.DeclareListContext):
        pass

    # Exit a parse tree produced by PhpParser#declareList.
    def exitDeclareList(self, ctx:PhpParser.DeclareListContext):
        pass


    # Enter a parse tree produced by PhpParser#formalParameterList.
    def enterFormalParameterList(self, ctx:PhpParser.FormalParameterListContext):
        pass

    # Exit a parse tree produced by PhpParser#formalParameterList.
    def exitFormalParameterList(self, ctx:PhpParser.FormalParameterListContext):
        pass


    # Enter a parse tree produced by PhpParser#formalParameter.
    def enterFormalParameter(self, ctx:PhpParser.FormalParameterContext):
        pass

    # Exit a parse tree produced by PhpParser#formalParameter.
    def exitFormalParameter(self, ctx:PhpParser.FormalParameterContext):
        pass


    # Enter a parse tree produced by PhpParser#typeHint.
    def enterTypeHint(self, ctx:PhpParser.TypeHintContext):
        pass

    # Exit a parse tree produced by PhpParser#typeHint.
    def exitTypeHint(self, ctx:PhpParser.TypeHintContext):
        pass


    # Enter a parse tree produced by PhpParser#globalStatement.
    def enterGlobalStatement(self, ctx:PhpParser.GlobalStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#globalStatement.
    def exitGlobalStatement(self, ctx:PhpParser.GlobalStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#globalVar.
    def enterGlobalVar(self, ctx:PhpParser.GlobalVarContext):
        pass

    # Exit a parse tree produced by PhpParser#globalVar.
    def exitGlobalVar(self, ctx:PhpParser.GlobalVarContext):
        pass


    # Enter a parse tree produced by PhpParser#echoStatement.
    def enterEchoStatement(self, ctx:PhpParser.EchoStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#echoStatement.
    def exitEchoStatement(self, ctx:PhpParser.EchoStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#staticVariableStatement.
    def enterStaticVariableStatement(self, ctx:PhpParser.StaticVariableStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#staticVariableStatement.
    def exitStaticVariableStatement(self, ctx:PhpParser.StaticVariableStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#classStatement.
    def enterClassStatement(self, ctx:PhpParser.ClassStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#classStatement.
    def exitClassStatement(self, ctx:PhpParser.ClassStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#traitAdaptations.
    def enterTraitAdaptations(self, ctx:PhpParser.TraitAdaptationsContext):
        pass

    # Exit a parse tree produced by PhpParser#traitAdaptations.
    def exitTraitAdaptations(self, ctx:PhpParser.TraitAdaptationsContext):
        pass


    # Enter a parse tree produced by PhpParser#traitAdaptationStatement.
    def enterTraitAdaptationStatement(self, ctx:PhpParser.TraitAdaptationStatementContext):
        pass

    # Exit a parse tree produced by PhpParser#traitAdaptationStatement.
    def exitTraitAdaptationStatement(self, ctx:PhpParser.TraitAdaptationStatementContext):
        pass


    # Enter a parse tree produced by PhpParser#traitPrecedence.
    def enterTraitPrecedence(self, ctx:PhpParser.TraitPrecedenceContext):
        pass

    # Exit a parse tree produced by PhpParser#traitPrecedence.
    def exitTraitPrecedence(self, ctx:PhpParser.TraitPrecedenceContext):
        pass


    # Enter a parse tree produced by PhpParser#traitAlias.
    def enterTraitAlias(self, ctx:PhpParser.TraitAliasContext):
        pass

    # Exit a parse tree produced by PhpParser#traitAlias.
    def exitTraitAlias(self, ctx:PhpParser.TraitAliasContext):
        pass


    # Enter a parse tree produced by PhpParser#traitMethodReference.
    def enterTraitMethodReference(self, ctx:PhpParser.TraitMethodReferenceContext):
        pass

    # Exit a parse tree produced by PhpParser#traitMethodReference.
    def exitTraitMethodReference(self, ctx:PhpParser.TraitMethodReferenceContext):
        pass


    # Enter a parse tree produced by PhpParser#baseCtorCall.
    def enterBaseCtorCall(self, ctx:PhpParser.BaseCtorCallContext):
        pass

    # Exit a parse tree produced by PhpParser#baseCtorCall.
    def exitBaseCtorCall(self, ctx:PhpParser.BaseCtorCallContext):
        pass


    # Enter a parse tree produced by PhpParser#methodBody.
    def enterMethodBody(self, ctx:PhpParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by PhpParser#methodBody.
    def exitMethodBody(self, ctx:PhpParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by PhpParser#propertyModifiers.
    def enterPropertyModifiers(self, ctx:PhpParser.PropertyModifiersContext):
        pass

    # Exit a parse tree produced by PhpParser#propertyModifiers.
    def exitPropertyModifiers(self, ctx:PhpParser.PropertyModifiersContext):
        pass


    # Enter a parse tree produced by PhpParser#memberModifiers.
    def enterMemberModifiers(self, ctx:PhpParser.MemberModifiersContext):
        pass

    # Exit a parse tree produced by PhpParser#memberModifiers.
    def exitMemberModifiers(self, ctx:PhpParser.MemberModifiersContext):
        pass


    # Enter a parse tree produced by PhpParser#variableInitializer.
    def enterVariableInitializer(self, ctx:PhpParser.VariableInitializerContext):
        pass

    # Exit a parse tree produced by PhpParser#variableInitializer.
    def exitVariableInitializer(self, ctx:PhpParser.VariableInitializerContext):
        pass


    # Enter a parse tree produced by PhpParser#identifierInitializer.
    def enterIdentifierInitializer(self, ctx:PhpParser.IdentifierInitializerContext):
        pass

    # Exit a parse tree produced by PhpParser#identifierInitializer.
    def exitIdentifierInitializer(self, ctx:PhpParser.IdentifierInitializerContext):
        pass


    # Enter a parse tree produced by PhpParser#globalConstantDeclaration.
    def enterGlobalConstantDeclaration(self, ctx:PhpParser.GlobalConstantDeclarationContext):
        pass

    # Exit a parse tree produced by PhpParser#globalConstantDeclaration.
    def exitGlobalConstantDeclaration(self, ctx:PhpParser.GlobalConstantDeclarationContext):
        pass


    # Enter a parse tree produced by PhpParser#expressionList.
    def enterExpressionList(self, ctx:PhpParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by PhpParser#expressionList.
    def exitExpressionList(self, ctx:PhpParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by PhpParser#parentheses.
    def enterParentheses(self, ctx:PhpParser.ParenthesesContext):
        pass

    # Exit a parse tree produced by PhpParser#parentheses.
    def exitParentheses(self, ctx:PhpParser.ParenthesesContext):
        pass


    # Enter a parse tree produced by PhpParser#ChainExpression.
    def enterChainExpression(self, ctx:PhpParser.ChainExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#ChainExpression.
    def exitChainExpression(self, ctx:PhpParser.ChainExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#SpecialWordExpression.
    def enterSpecialWordExpression(self, ctx:PhpParser.SpecialWordExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#SpecialWordExpression.
    def exitSpecialWordExpression(self, ctx:PhpParser.SpecialWordExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#ArrayCreationExpression.
    def enterArrayCreationExpression(self, ctx:PhpParser.ArrayCreationExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#ArrayCreationExpression.
    def exitArrayCreationExpression(self, ctx:PhpParser.ArrayCreationExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#BackQuoteStringExpression.
    def enterBackQuoteStringExpression(self, ctx:PhpParser.BackQuoteStringExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#BackQuoteStringExpression.
    def exitBackQuoteStringExpression(self, ctx:PhpParser.BackQuoteStringExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#MatchExpression.
    def enterMatchExpression(self, ctx:PhpParser.MatchExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#MatchExpression.
    def exitMatchExpression(self, ctx:PhpParser.MatchExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#LogicalExpression.
    def enterLogicalExpression(self, ctx:PhpParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#LogicalExpression.
    def exitLogicalExpression(self, ctx:PhpParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#PrintExpression.
    def enterPrintExpression(self, ctx:PhpParser.PrintExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#PrintExpression.
    def exitPrintExpression(self, ctx:PhpParser.PrintExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#AssignmentExpression.
    def enterAssignmentExpression(self, ctx:PhpParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#AssignmentExpression.
    def exitAssignmentExpression(self, ctx:PhpParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#PostfixIncDecExpression.
    def enterPostfixIncDecExpression(self, ctx:PhpParser.PostfixIncDecExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#PostfixIncDecExpression.
    def exitPostfixIncDecExpression(self, ctx:PhpParser.PostfixIncDecExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#CloneExpression.
    def enterCloneExpression(self, ctx:PhpParser.CloneExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#CloneExpression.
    def exitCloneExpression(self, ctx:PhpParser.CloneExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#UnaryOperatorExpression.
    def enterUnaryOperatorExpression(self, ctx:PhpParser.UnaryOperatorExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#UnaryOperatorExpression.
    def exitUnaryOperatorExpression(self, ctx:PhpParser.UnaryOperatorExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#NewExpression.
    def enterNewExpression(self, ctx:PhpParser.NewExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#NewExpression.
    def exitNewExpression(self, ctx:PhpParser.NewExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#ParenthesisExpression.
    def enterParenthesisExpression(self, ctx:PhpParser.ParenthesisExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#ParenthesisExpression.
    def exitParenthesisExpression(self, ctx:PhpParser.ParenthesisExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#SpaceshipExpression.
    def enterSpaceshipExpression(self, ctx:PhpParser.SpaceshipExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#SpaceshipExpression.
    def exitSpaceshipExpression(self, ctx:PhpParser.SpaceshipExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#ConditionalExpression.
    def enterConditionalExpression(self, ctx:PhpParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#ConditionalExpression.
    def exitConditionalExpression(self, ctx:PhpParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#NullCoalescingExpression.
    def enterNullCoalescingExpression(self, ctx:PhpParser.NullCoalescingExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#NullCoalescingExpression.
    def exitNullCoalescingExpression(self, ctx:PhpParser.NullCoalescingExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#ArithmeticExpression.
    def enterArithmeticExpression(self, ctx:PhpParser.ArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#ArithmeticExpression.
    def exitArithmeticExpression(self, ctx:PhpParser.ArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#IndexerExpression.
    def enterIndexerExpression(self, ctx:PhpParser.IndexerExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#IndexerExpression.
    def exitIndexerExpression(self, ctx:PhpParser.IndexerExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#ScalarExpression.
    def enterScalarExpression(self, ctx:PhpParser.ScalarExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#ScalarExpression.
    def exitScalarExpression(self, ctx:PhpParser.ScalarExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#PrefixIncDecExpression.
    def enterPrefixIncDecExpression(self, ctx:PhpParser.PrefixIncDecExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#PrefixIncDecExpression.
    def exitPrefixIncDecExpression(self, ctx:PhpParser.PrefixIncDecExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#ComparisonExpression.
    def enterComparisonExpression(self, ctx:PhpParser.ComparisonExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#ComparisonExpression.
    def exitComparisonExpression(self, ctx:PhpParser.ComparisonExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#CastExpression.
    def enterCastExpression(self, ctx:PhpParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#CastExpression.
    def exitCastExpression(self, ctx:PhpParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#InstanceOfExpression.
    def enterInstanceOfExpression(self, ctx:PhpParser.InstanceOfExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#InstanceOfExpression.
    def exitInstanceOfExpression(self, ctx:PhpParser.InstanceOfExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#LambdaFunctionExpression.
    def enterLambdaFunctionExpression(self, ctx:PhpParser.LambdaFunctionExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#LambdaFunctionExpression.
    def exitLambdaFunctionExpression(self, ctx:PhpParser.LambdaFunctionExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#BitwiseExpression.
    def enterBitwiseExpression(self, ctx:PhpParser.BitwiseExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#BitwiseExpression.
    def exitBitwiseExpression(self, ctx:PhpParser.BitwiseExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#assignable.
    def enterAssignable(self, ctx:PhpParser.AssignableContext):
        pass

    # Exit a parse tree produced by PhpParser#assignable.
    def exitAssignable(self, ctx:PhpParser.AssignableContext):
        pass


    # Enter a parse tree produced by PhpParser#arrayCreation.
    def enterArrayCreation(self, ctx:PhpParser.ArrayCreationContext):
        pass

    # Exit a parse tree produced by PhpParser#arrayCreation.
    def exitArrayCreation(self, ctx:PhpParser.ArrayCreationContext):
        pass


    # Enter a parse tree produced by PhpParser#lambdaFunctionExpr.
    def enterLambdaFunctionExpr(self, ctx:PhpParser.LambdaFunctionExprContext):
        pass

    # Exit a parse tree produced by PhpParser#lambdaFunctionExpr.
    def exitLambdaFunctionExpr(self, ctx:PhpParser.LambdaFunctionExprContext):
        pass


    # Enter a parse tree produced by PhpParser#matchExpr.
    def enterMatchExpr(self, ctx:PhpParser.MatchExprContext):
        pass

    # Exit a parse tree produced by PhpParser#matchExpr.
    def exitMatchExpr(self, ctx:PhpParser.MatchExprContext):
        pass


    # Enter a parse tree produced by PhpParser#matchItem.
    def enterMatchItem(self, ctx:PhpParser.MatchItemContext):
        pass

    # Exit a parse tree produced by PhpParser#matchItem.
    def exitMatchItem(self, ctx:PhpParser.MatchItemContext):
        pass


    # Enter a parse tree produced by PhpParser#newExpr.
    def enterNewExpr(self, ctx:PhpParser.NewExprContext):
        pass

    # Exit a parse tree produced by PhpParser#newExpr.
    def exitNewExpr(self, ctx:PhpParser.NewExprContext):
        pass


    # Enter a parse tree produced by PhpParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:PhpParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by PhpParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:PhpParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by PhpParser#yieldExpression.
    def enterYieldExpression(self, ctx:PhpParser.YieldExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#yieldExpression.
    def exitYieldExpression(self, ctx:PhpParser.YieldExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#arrayItemList.
    def enterArrayItemList(self, ctx:PhpParser.ArrayItemListContext):
        pass

    # Exit a parse tree produced by PhpParser#arrayItemList.
    def exitArrayItemList(self, ctx:PhpParser.ArrayItemListContext):
        pass


    # Enter a parse tree produced by PhpParser#arrayItem.
    def enterArrayItem(self, ctx:PhpParser.ArrayItemContext):
        pass

    # Exit a parse tree produced by PhpParser#arrayItem.
    def exitArrayItem(self, ctx:PhpParser.ArrayItemContext):
        pass


    # Enter a parse tree produced by PhpParser#lambdaFunctionUseVars.
    def enterLambdaFunctionUseVars(self, ctx:PhpParser.LambdaFunctionUseVarsContext):
        pass

    # Exit a parse tree produced by PhpParser#lambdaFunctionUseVars.
    def exitLambdaFunctionUseVars(self, ctx:PhpParser.LambdaFunctionUseVarsContext):
        pass


    # Enter a parse tree produced by PhpParser#lambdaFunctionUseVar.
    def enterLambdaFunctionUseVar(self, ctx:PhpParser.LambdaFunctionUseVarContext):
        pass

    # Exit a parse tree produced by PhpParser#lambdaFunctionUseVar.
    def exitLambdaFunctionUseVar(self, ctx:PhpParser.LambdaFunctionUseVarContext):
        pass


    # Enter a parse tree produced by PhpParser#qualifiedStaticTypeRef.
    def enterQualifiedStaticTypeRef(self, ctx:PhpParser.QualifiedStaticTypeRefContext):
        pass

    # Exit a parse tree produced by PhpParser#qualifiedStaticTypeRef.
    def exitQualifiedStaticTypeRef(self, ctx:PhpParser.QualifiedStaticTypeRefContext):
        pass


    # Enter a parse tree produced by PhpParser#typeRef.
    def enterTypeRef(self, ctx:PhpParser.TypeRefContext):
        pass

    # Exit a parse tree produced by PhpParser#typeRef.
    def exitTypeRef(self, ctx:PhpParser.TypeRefContext):
        pass


    # Enter a parse tree produced by PhpParser#anonymousClass.
    def enterAnonymousClass(self, ctx:PhpParser.AnonymousClassContext):
        pass

    # Exit a parse tree produced by PhpParser#anonymousClass.
    def exitAnonymousClass(self, ctx:PhpParser.AnonymousClassContext):
        pass


    # Enter a parse tree produced by PhpParser#indirectTypeRef.
    def enterIndirectTypeRef(self, ctx:PhpParser.IndirectTypeRefContext):
        pass

    # Exit a parse tree produced by PhpParser#indirectTypeRef.
    def exitIndirectTypeRef(self, ctx:PhpParser.IndirectTypeRefContext):
        pass


    # Enter a parse tree produced by PhpParser#qualifiedNamespaceName.
    def enterQualifiedNamespaceName(self, ctx:PhpParser.QualifiedNamespaceNameContext):
        pass

    # Exit a parse tree produced by PhpParser#qualifiedNamespaceName.
    def exitQualifiedNamespaceName(self, ctx:PhpParser.QualifiedNamespaceNameContext):
        pass


    # Enter a parse tree produced by PhpParser#namespaceNameList.
    def enterNamespaceNameList(self, ctx:PhpParser.NamespaceNameListContext):
        pass

    # Exit a parse tree produced by PhpParser#namespaceNameList.
    def exitNamespaceNameList(self, ctx:PhpParser.NamespaceNameListContext):
        pass


    # Enter a parse tree produced by PhpParser#namespaceNameTail.
    def enterNamespaceNameTail(self, ctx:PhpParser.NamespaceNameTailContext):
        pass

    # Exit a parse tree produced by PhpParser#namespaceNameTail.
    def exitNamespaceNameTail(self, ctx:PhpParser.NamespaceNameTailContext):
        pass


    # Enter a parse tree produced by PhpParser#qualifiedNamespaceNameList.
    def enterQualifiedNamespaceNameList(self, ctx:PhpParser.QualifiedNamespaceNameListContext):
        pass

    # Exit a parse tree produced by PhpParser#qualifiedNamespaceNameList.
    def exitQualifiedNamespaceNameList(self, ctx:PhpParser.QualifiedNamespaceNameListContext):
        pass


    # Enter a parse tree produced by PhpParser#arguments.
    def enterArguments(self, ctx:PhpParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by PhpParser#arguments.
    def exitArguments(self, ctx:PhpParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by PhpParser#actualArgument.
    def enterActualArgument(self, ctx:PhpParser.ActualArgumentContext):
        pass

    # Exit a parse tree produced by PhpParser#actualArgument.
    def exitActualArgument(self, ctx:PhpParser.ActualArgumentContext):
        pass


    # Enter a parse tree produced by PhpParser#argumentName.
    def enterArgumentName(self, ctx:PhpParser.ArgumentNameContext):
        pass

    # Exit a parse tree produced by PhpParser#argumentName.
    def exitArgumentName(self, ctx:PhpParser.ArgumentNameContext):
        pass


    # Enter a parse tree produced by PhpParser#constantInitializer.
    def enterConstantInitializer(self, ctx:PhpParser.ConstantInitializerContext):
        pass

    # Exit a parse tree produced by PhpParser#constantInitializer.
    def exitConstantInitializer(self, ctx:PhpParser.ConstantInitializerContext):
        pass


    # Enter a parse tree produced by PhpParser#constant.
    def enterConstant(self, ctx:PhpParser.ConstantContext):
        pass

    # Exit a parse tree produced by PhpParser#constant.
    def exitConstant(self, ctx:PhpParser.ConstantContext):
        pass


    # Enter a parse tree produced by PhpParser#literalConstant.
    def enterLiteralConstant(self, ctx:PhpParser.LiteralConstantContext):
        pass

    # Exit a parse tree produced by PhpParser#literalConstant.
    def exitLiteralConstant(self, ctx:PhpParser.LiteralConstantContext):
        pass


    # Enter a parse tree produced by PhpParser#numericConstant.
    def enterNumericConstant(self, ctx:PhpParser.NumericConstantContext):
        pass

    # Exit a parse tree produced by PhpParser#numericConstant.
    def exitNumericConstant(self, ctx:PhpParser.NumericConstantContext):
        pass


    # Enter a parse tree produced by PhpParser#classConstant.
    def enterClassConstant(self, ctx:PhpParser.ClassConstantContext):
        pass

    # Exit a parse tree produced by PhpParser#classConstant.
    def exitClassConstant(self, ctx:PhpParser.ClassConstantContext):
        pass


    # Enter a parse tree produced by PhpParser#stringConstant.
    def enterStringConstant(self, ctx:PhpParser.StringConstantContext):
        pass

    # Exit a parse tree produced by PhpParser#stringConstant.
    def exitStringConstant(self, ctx:PhpParser.StringConstantContext):
        pass


    # Enter a parse tree produced by PhpParser#string.
    def enterString(self, ctx:PhpParser.StringContext):
        pass

    # Exit a parse tree produced by PhpParser#string.
    def exitString(self, ctx:PhpParser.StringContext):
        pass


    # Enter a parse tree produced by PhpParser#interpolatedStringPart.
    def enterInterpolatedStringPart(self, ctx:PhpParser.InterpolatedStringPartContext):
        pass

    # Exit a parse tree produced by PhpParser#interpolatedStringPart.
    def exitInterpolatedStringPart(self, ctx:PhpParser.InterpolatedStringPartContext):
        pass


    # Enter a parse tree produced by PhpParser#chainList.
    def enterChainList(self, ctx:PhpParser.ChainListContext):
        pass

    # Exit a parse tree produced by PhpParser#chainList.
    def exitChainList(self, ctx:PhpParser.ChainListContext):
        pass


    # Enter a parse tree produced by PhpParser#chain.
    def enterChain(self, ctx:PhpParser.ChainContext):
        pass

    # Exit a parse tree produced by PhpParser#chain.
    def exitChain(self, ctx:PhpParser.ChainContext):
        pass


    # Enter a parse tree produced by PhpParser#chainOrigin.
    def enterChainOrigin(self, ctx:PhpParser.ChainOriginContext):
        pass

    # Exit a parse tree produced by PhpParser#chainOrigin.
    def exitChainOrigin(self, ctx:PhpParser.ChainOriginContext):
        pass


    # Enter a parse tree produced by PhpParser#memberAccess.
    def enterMemberAccess(self, ctx:PhpParser.MemberAccessContext):
        pass

    # Exit a parse tree produced by PhpParser#memberAccess.
    def exitMemberAccess(self, ctx:PhpParser.MemberAccessContext):
        pass


    # Enter a parse tree produced by PhpParser#functionCall.
    def enterFunctionCall(self, ctx:PhpParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by PhpParser#functionCall.
    def exitFunctionCall(self, ctx:PhpParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by PhpParser#functionCallName.
    def enterFunctionCallName(self, ctx:PhpParser.FunctionCallNameContext):
        pass

    # Exit a parse tree produced by PhpParser#functionCallName.
    def exitFunctionCallName(self, ctx:PhpParser.FunctionCallNameContext):
        pass


    # Enter a parse tree produced by PhpParser#actualArguments.
    def enterActualArguments(self, ctx:PhpParser.ActualArgumentsContext):
        pass

    # Exit a parse tree produced by PhpParser#actualArguments.
    def exitActualArguments(self, ctx:PhpParser.ActualArgumentsContext):
        pass


    # Enter a parse tree produced by PhpParser#chainBase.
    def enterChainBase(self, ctx:PhpParser.ChainBaseContext):
        pass

    # Exit a parse tree produced by PhpParser#chainBase.
    def exitChainBase(self, ctx:PhpParser.ChainBaseContext):
        pass


    # Enter a parse tree produced by PhpParser#keyedFieldName.
    def enterKeyedFieldName(self, ctx:PhpParser.KeyedFieldNameContext):
        pass

    # Exit a parse tree produced by PhpParser#keyedFieldName.
    def exitKeyedFieldName(self, ctx:PhpParser.KeyedFieldNameContext):
        pass


    # Enter a parse tree produced by PhpParser#keyedSimpleFieldName.
    def enterKeyedSimpleFieldName(self, ctx:PhpParser.KeyedSimpleFieldNameContext):
        pass

    # Exit a parse tree produced by PhpParser#keyedSimpleFieldName.
    def exitKeyedSimpleFieldName(self, ctx:PhpParser.KeyedSimpleFieldNameContext):
        pass


    # Enter a parse tree produced by PhpParser#keyedVariable.
    def enterKeyedVariable(self, ctx:PhpParser.KeyedVariableContext):
        pass

    # Exit a parse tree produced by PhpParser#keyedVariable.
    def exitKeyedVariable(self, ctx:PhpParser.KeyedVariableContext):
        pass


    # Enter a parse tree produced by PhpParser#squareCurlyExpression.
    def enterSquareCurlyExpression(self, ctx:PhpParser.SquareCurlyExpressionContext):
        pass

    # Exit a parse tree produced by PhpParser#squareCurlyExpression.
    def exitSquareCurlyExpression(self, ctx:PhpParser.SquareCurlyExpressionContext):
        pass


    # Enter a parse tree produced by PhpParser#assignmentList.
    def enterAssignmentList(self, ctx:PhpParser.AssignmentListContext):
        pass

    # Exit a parse tree produced by PhpParser#assignmentList.
    def exitAssignmentList(self, ctx:PhpParser.AssignmentListContext):
        pass


    # Enter a parse tree produced by PhpParser#assignmentListElement.
    def enterAssignmentListElement(self, ctx:PhpParser.AssignmentListElementContext):
        pass

    # Exit a parse tree produced by PhpParser#assignmentListElement.
    def exitAssignmentListElement(self, ctx:PhpParser.AssignmentListElementContext):
        pass


    # Enter a parse tree produced by PhpParser#modifier.
    def enterModifier(self, ctx:PhpParser.ModifierContext):
        pass

    # Exit a parse tree produced by PhpParser#modifier.
    def exitModifier(self, ctx:PhpParser.ModifierContext):
        pass


    # Enter a parse tree produced by PhpParser#identifier.
    def enterIdentifier(self, ctx:PhpParser.IdentifierContext):
        pass

    # Exit a parse tree produced by PhpParser#identifier.
    def exitIdentifier(self, ctx:PhpParser.IdentifierContext):
        pass


    # Enter a parse tree produced by PhpParser#memberModifier.
    def enterMemberModifier(self, ctx:PhpParser.MemberModifierContext):
        pass

    # Exit a parse tree produced by PhpParser#memberModifier.
    def exitMemberModifier(self, ctx:PhpParser.MemberModifierContext):
        pass


    # Enter a parse tree produced by PhpParser#magicConstant.
    def enterMagicConstant(self, ctx:PhpParser.MagicConstantContext):
        pass

    # Exit a parse tree produced by PhpParser#magicConstant.
    def exitMagicConstant(self, ctx:PhpParser.MagicConstantContext):
        pass


    # Enter a parse tree produced by PhpParser#magicMethod.
    def enterMagicMethod(self, ctx:PhpParser.MagicMethodContext):
        pass

    # Exit a parse tree produced by PhpParser#magicMethod.
    def exitMagicMethod(self, ctx:PhpParser.MagicMethodContext):
        pass


    # Enter a parse tree produced by PhpParser#primitiveType.
    def enterPrimitiveType(self, ctx:PhpParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by PhpParser#primitiveType.
    def exitPrimitiveType(self, ctx:PhpParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by PhpParser#castOperation.
    def enterCastOperation(self, ctx:PhpParser.CastOperationContext):
        pass

    # Exit a parse tree produced by PhpParser#castOperation.
    def exitCastOperation(self, ctx:PhpParser.CastOperationContext):
        pass



del PhpParser