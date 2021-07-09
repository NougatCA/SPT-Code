# Generated from Java8Parser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Java8Parser import Java8Parser
else:
    from Java8Parser import Java8Parser

# This class defines a complete listener for a parse tree produced by Java8Parser.
class Java8ParserListener(ParseTreeListener):

    # Enter a parse tree produced by Java8Parser#literal.
    def enterLiteral(self, ctx:Java8Parser.LiteralContext):
        pass

    # Exit a parse tree produced by Java8Parser#literal.
    def exitLiteral(self, ctx:Java8Parser.LiteralContext):
        pass


    # Enter a parse tree produced by Java8Parser#primitiveType.
    def enterPrimitiveType(self, ctx:Java8Parser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#primitiveType.
    def exitPrimitiveType(self, ctx:Java8Parser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#numericType.
    def enterNumericType(self, ctx:Java8Parser.NumericTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#numericType.
    def exitNumericType(self, ctx:Java8Parser.NumericTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#integralType.
    def enterIntegralType(self, ctx:Java8Parser.IntegralTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#integralType.
    def exitIntegralType(self, ctx:Java8Parser.IntegralTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#floatingPointType.
    def enterFloatingPointType(self, ctx:Java8Parser.FloatingPointTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#floatingPointType.
    def exitFloatingPointType(self, ctx:Java8Parser.FloatingPointTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#referenceType.
    def enterReferenceType(self, ctx:Java8Parser.ReferenceTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#referenceType.
    def exitReferenceType(self, ctx:Java8Parser.ReferenceTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#classOrInterfaceType.
    def enterClassOrInterfaceType(self, ctx:Java8Parser.ClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#classOrInterfaceType.
    def exitClassOrInterfaceType(self, ctx:Java8Parser.ClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#classType.
    def enterClassType(self, ctx:Java8Parser.ClassTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#classType.
    def exitClassType(self, ctx:Java8Parser.ClassTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#classType_lf_classOrInterfaceType.
    def enterClassType_lf_classOrInterfaceType(self, ctx:Java8Parser.ClassType_lf_classOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#classType_lf_classOrInterfaceType.
    def exitClassType_lf_classOrInterfaceType(self, ctx:Java8Parser.ClassType_lf_classOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#classType_lfno_classOrInterfaceType.
    def enterClassType_lfno_classOrInterfaceType(self, ctx:Java8Parser.ClassType_lfno_classOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#classType_lfno_classOrInterfaceType.
    def exitClassType_lfno_classOrInterfaceType(self, ctx:Java8Parser.ClassType_lfno_classOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#interfaceType.
    def enterInterfaceType(self, ctx:Java8Parser.InterfaceTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#interfaceType.
    def exitInterfaceType(self, ctx:Java8Parser.InterfaceTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#interfaceType_lf_classOrInterfaceType.
    def enterInterfaceType_lf_classOrInterfaceType(self, ctx:Java8Parser.InterfaceType_lf_classOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#interfaceType_lf_classOrInterfaceType.
    def exitInterfaceType_lf_classOrInterfaceType(self, ctx:Java8Parser.InterfaceType_lf_classOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#interfaceType_lfno_classOrInterfaceType.
    def enterInterfaceType_lfno_classOrInterfaceType(self, ctx:Java8Parser.InterfaceType_lfno_classOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#interfaceType_lfno_classOrInterfaceType.
    def exitInterfaceType_lfno_classOrInterfaceType(self, ctx:Java8Parser.InterfaceType_lfno_classOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#typeVariable.
    def enterTypeVariable(self, ctx:Java8Parser.TypeVariableContext):
        pass

    # Exit a parse tree produced by Java8Parser#typeVariable.
    def exitTypeVariable(self, ctx:Java8Parser.TypeVariableContext):
        pass


    # Enter a parse tree produced by Java8Parser#arrayType.
    def enterArrayType(self, ctx:Java8Parser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#arrayType.
    def exitArrayType(self, ctx:Java8Parser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#dims.
    def enterDims(self, ctx:Java8Parser.DimsContext):
        pass

    # Exit a parse tree produced by Java8Parser#dims.
    def exitDims(self, ctx:Java8Parser.DimsContext):
        pass


    # Enter a parse tree produced by Java8Parser#typeParameter.
    def enterTypeParameter(self, ctx:Java8Parser.TypeParameterContext):
        pass

    # Exit a parse tree produced by Java8Parser#typeParameter.
    def exitTypeParameter(self, ctx:Java8Parser.TypeParameterContext):
        pass


    # Enter a parse tree produced by Java8Parser#typeParameterModifier.
    def enterTypeParameterModifier(self, ctx:Java8Parser.TypeParameterModifierContext):
        pass

    # Exit a parse tree produced by Java8Parser#typeParameterModifier.
    def exitTypeParameterModifier(self, ctx:Java8Parser.TypeParameterModifierContext):
        pass


    # Enter a parse tree produced by Java8Parser#typeBound.
    def enterTypeBound(self, ctx:Java8Parser.TypeBoundContext):
        pass

    # Exit a parse tree produced by Java8Parser#typeBound.
    def exitTypeBound(self, ctx:Java8Parser.TypeBoundContext):
        pass


    # Enter a parse tree produced by Java8Parser#additionalBound.
    def enterAdditionalBound(self, ctx:Java8Parser.AdditionalBoundContext):
        pass

    # Exit a parse tree produced by Java8Parser#additionalBound.
    def exitAdditionalBound(self, ctx:Java8Parser.AdditionalBoundContext):
        pass


    # Enter a parse tree produced by Java8Parser#typeArguments.
    def enterTypeArguments(self, ctx:Java8Parser.TypeArgumentsContext):
        pass

    # Exit a parse tree produced by Java8Parser#typeArguments.
    def exitTypeArguments(self, ctx:Java8Parser.TypeArgumentsContext):
        pass


    # Enter a parse tree produced by Java8Parser#typeArgumentList.
    def enterTypeArgumentList(self, ctx:Java8Parser.TypeArgumentListContext):
        pass

    # Exit a parse tree produced by Java8Parser#typeArgumentList.
    def exitTypeArgumentList(self, ctx:Java8Parser.TypeArgumentListContext):
        pass


    # Enter a parse tree produced by Java8Parser#typeArgument.
    def enterTypeArgument(self, ctx:Java8Parser.TypeArgumentContext):
        pass

    # Exit a parse tree produced by Java8Parser#typeArgument.
    def exitTypeArgument(self, ctx:Java8Parser.TypeArgumentContext):
        pass


    # Enter a parse tree produced by Java8Parser#wildcard.
    def enterWildcard(self, ctx:Java8Parser.WildcardContext):
        pass

    # Exit a parse tree produced by Java8Parser#wildcard.
    def exitWildcard(self, ctx:Java8Parser.WildcardContext):
        pass


    # Enter a parse tree produced by Java8Parser#wildcardBounds.
    def enterWildcardBounds(self, ctx:Java8Parser.WildcardBoundsContext):
        pass

    # Exit a parse tree produced by Java8Parser#wildcardBounds.
    def exitWildcardBounds(self, ctx:Java8Parser.WildcardBoundsContext):
        pass


    # Enter a parse tree produced by Java8Parser#packageName.
    def enterPackageName(self, ctx:Java8Parser.PackageNameContext):
        pass

    # Exit a parse tree produced by Java8Parser#packageName.
    def exitPackageName(self, ctx:Java8Parser.PackageNameContext):
        pass


    # Enter a parse tree produced by Java8Parser#typeName.
    def enterTypeName(self, ctx:Java8Parser.TypeNameContext):
        pass

    # Exit a parse tree produced by Java8Parser#typeName.
    def exitTypeName(self, ctx:Java8Parser.TypeNameContext):
        pass


    # Enter a parse tree produced by Java8Parser#packageOrTypeName.
    def enterPackageOrTypeName(self, ctx:Java8Parser.PackageOrTypeNameContext):
        pass

    # Exit a parse tree produced by Java8Parser#packageOrTypeName.
    def exitPackageOrTypeName(self, ctx:Java8Parser.PackageOrTypeNameContext):
        pass


    # Enter a parse tree produced by Java8Parser#expressionName.
    def enterExpressionName(self, ctx:Java8Parser.ExpressionNameContext):
        pass

    # Exit a parse tree produced by Java8Parser#expressionName.
    def exitExpressionName(self, ctx:Java8Parser.ExpressionNameContext):
        pass


    # Enter a parse tree produced by Java8Parser#methodName.
    def enterMethodName(self, ctx:Java8Parser.MethodNameContext):
        pass

    # Exit a parse tree produced by Java8Parser#methodName.
    def exitMethodName(self, ctx:Java8Parser.MethodNameContext):
        pass


    # Enter a parse tree produced by Java8Parser#ambiguousName.
    def enterAmbiguousName(self, ctx:Java8Parser.AmbiguousNameContext):
        pass

    # Exit a parse tree produced by Java8Parser#ambiguousName.
    def exitAmbiguousName(self, ctx:Java8Parser.AmbiguousNameContext):
        pass


    # Enter a parse tree produced by Java8Parser#compilationUnit.
    def enterCompilationUnit(self, ctx:Java8Parser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by Java8Parser#compilationUnit.
    def exitCompilationUnit(self, ctx:Java8Parser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by Java8Parser#packageDeclaration.
    def enterPackageDeclaration(self, ctx:Java8Parser.PackageDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#packageDeclaration.
    def exitPackageDeclaration(self, ctx:Java8Parser.PackageDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#packageModifier.
    def enterPackageModifier(self, ctx:Java8Parser.PackageModifierContext):
        pass

    # Exit a parse tree produced by Java8Parser#packageModifier.
    def exitPackageModifier(self, ctx:Java8Parser.PackageModifierContext):
        pass


    # Enter a parse tree produced by Java8Parser#importDeclaration.
    def enterImportDeclaration(self, ctx:Java8Parser.ImportDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#importDeclaration.
    def exitImportDeclaration(self, ctx:Java8Parser.ImportDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#singleTypeImportDeclaration.
    def enterSingleTypeImportDeclaration(self, ctx:Java8Parser.SingleTypeImportDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#singleTypeImportDeclaration.
    def exitSingleTypeImportDeclaration(self, ctx:Java8Parser.SingleTypeImportDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#typeImportOnDemandDeclaration.
    def enterTypeImportOnDemandDeclaration(self, ctx:Java8Parser.TypeImportOnDemandDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#typeImportOnDemandDeclaration.
    def exitTypeImportOnDemandDeclaration(self, ctx:Java8Parser.TypeImportOnDemandDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#singleStaticImportDeclaration.
    def enterSingleStaticImportDeclaration(self, ctx:Java8Parser.SingleStaticImportDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#singleStaticImportDeclaration.
    def exitSingleStaticImportDeclaration(self, ctx:Java8Parser.SingleStaticImportDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#staticImportOnDemandDeclaration.
    def enterStaticImportOnDemandDeclaration(self, ctx:Java8Parser.StaticImportOnDemandDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#staticImportOnDemandDeclaration.
    def exitStaticImportOnDemandDeclaration(self, ctx:Java8Parser.StaticImportOnDemandDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:Java8Parser.TypeDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#typeDeclaration.
    def exitTypeDeclaration(self, ctx:Java8Parser.TypeDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#classDeclaration.
    def enterClassDeclaration(self, ctx:Java8Parser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#classDeclaration.
    def exitClassDeclaration(self, ctx:Java8Parser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#normalClassDeclaration.
    def enterNormalClassDeclaration(self, ctx:Java8Parser.NormalClassDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#normalClassDeclaration.
    def exitNormalClassDeclaration(self, ctx:Java8Parser.NormalClassDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#classModifier.
    def enterClassModifier(self, ctx:Java8Parser.ClassModifierContext):
        pass

    # Exit a parse tree produced by Java8Parser#classModifier.
    def exitClassModifier(self, ctx:Java8Parser.ClassModifierContext):
        pass


    # Enter a parse tree produced by Java8Parser#typeParameters.
    def enterTypeParameters(self, ctx:Java8Parser.TypeParametersContext):
        pass

    # Exit a parse tree produced by Java8Parser#typeParameters.
    def exitTypeParameters(self, ctx:Java8Parser.TypeParametersContext):
        pass


    # Enter a parse tree produced by Java8Parser#typeParameterList.
    def enterTypeParameterList(self, ctx:Java8Parser.TypeParameterListContext):
        pass

    # Exit a parse tree produced by Java8Parser#typeParameterList.
    def exitTypeParameterList(self, ctx:Java8Parser.TypeParameterListContext):
        pass


    # Enter a parse tree produced by Java8Parser#superclass.
    def enterSuperclass(self, ctx:Java8Parser.SuperclassContext):
        pass

    # Exit a parse tree produced by Java8Parser#superclass.
    def exitSuperclass(self, ctx:Java8Parser.SuperclassContext):
        pass


    # Enter a parse tree produced by Java8Parser#superinterfaces.
    def enterSuperinterfaces(self, ctx:Java8Parser.SuperinterfacesContext):
        pass

    # Exit a parse tree produced by Java8Parser#superinterfaces.
    def exitSuperinterfaces(self, ctx:Java8Parser.SuperinterfacesContext):
        pass


    # Enter a parse tree produced by Java8Parser#interfaceTypeList.
    def enterInterfaceTypeList(self, ctx:Java8Parser.InterfaceTypeListContext):
        pass

    # Exit a parse tree produced by Java8Parser#interfaceTypeList.
    def exitInterfaceTypeList(self, ctx:Java8Parser.InterfaceTypeListContext):
        pass


    # Enter a parse tree produced by Java8Parser#classBody.
    def enterClassBody(self, ctx:Java8Parser.ClassBodyContext):
        pass

    # Exit a parse tree produced by Java8Parser#classBody.
    def exitClassBody(self, ctx:Java8Parser.ClassBodyContext):
        pass


    # Enter a parse tree produced by Java8Parser#classBodyDeclaration.
    def enterClassBodyDeclaration(self, ctx:Java8Parser.ClassBodyDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#classBodyDeclaration.
    def exitClassBodyDeclaration(self, ctx:Java8Parser.ClassBodyDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#classMemberDeclaration.
    def enterClassMemberDeclaration(self, ctx:Java8Parser.ClassMemberDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#classMemberDeclaration.
    def exitClassMemberDeclaration(self, ctx:Java8Parser.ClassMemberDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:Java8Parser.FieldDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#fieldDeclaration.
    def exitFieldDeclaration(self, ctx:Java8Parser.FieldDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#fieldModifier.
    def enterFieldModifier(self, ctx:Java8Parser.FieldModifierContext):
        pass

    # Exit a parse tree produced by Java8Parser#fieldModifier.
    def exitFieldModifier(self, ctx:Java8Parser.FieldModifierContext):
        pass


    # Enter a parse tree produced by Java8Parser#variableDeclaratorList.
    def enterVariableDeclaratorList(self, ctx:Java8Parser.VariableDeclaratorListContext):
        pass

    # Exit a parse tree produced by Java8Parser#variableDeclaratorList.
    def exitVariableDeclaratorList(self, ctx:Java8Parser.VariableDeclaratorListContext):
        pass


    # Enter a parse tree produced by Java8Parser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:Java8Parser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by Java8Parser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:Java8Parser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by Java8Parser#variableDeclaratorId.
    def enterVariableDeclaratorId(self, ctx:Java8Parser.VariableDeclaratorIdContext):
        pass

    # Exit a parse tree produced by Java8Parser#variableDeclaratorId.
    def exitVariableDeclaratorId(self, ctx:Java8Parser.VariableDeclaratorIdContext):
        pass


    # Enter a parse tree produced by Java8Parser#variableInitializer.
    def enterVariableInitializer(self, ctx:Java8Parser.VariableInitializerContext):
        pass

    # Exit a parse tree produced by Java8Parser#variableInitializer.
    def exitVariableInitializer(self, ctx:Java8Parser.VariableInitializerContext):
        pass


    # Enter a parse tree produced by Java8Parser#unannType.
    def enterUnannType(self, ctx:Java8Parser.UnannTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#unannType.
    def exitUnannType(self, ctx:Java8Parser.UnannTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#unannPrimitiveType.
    def enterUnannPrimitiveType(self, ctx:Java8Parser.UnannPrimitiveTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#unannPrimitiveType.
    def exitUnannPrimitiveType(self, ctx:Java8Parser.UnannPrimitiveTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#unannReferenceType.
    def enterUnannReferenceType(self, ctx:Java8Parser.UnannReferenceTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#unannReferenceType.
    def exitUnannReferenceType(self, ctx:Java8Parser.UnannReferenceTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#unannClassOrInterfaceType.
    def enterUnannClassOrInterfaceType(self, ctx:Java8Parser.UnannClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#unannClassOrInterfaceType.
    def exitUnannClassOrInterfaceType(self, ctx:Java8Parser.UnannClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#unannClassType.
    def enterUnannClassType(self, ctx:Java8Parser.UnannClassTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#unannClassType.
    def exitUnannClassType(self, ctx:Java8Parser.UnannClassTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#unannClassType_lf_unannClassOrInterfaceType.
    def enterUnannClassType_lf_unannClassOrInterfaceType(self, ctx:Java8Parser.UnannClassType_lf_unannClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#unannClassType_lf_unannClassOrInterfaceType.
    def exitUnannClassType_lf_unannClassOrInterfaceType(self, ctx:Java8Parser.UnannClassType_lf_unannClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#unannClassType_lfno_unannClassOrInterfaceType.
    def enterUnannClassType_lfno_unannClassOrInterfaceType(self, ctx:Java8Parser.UnannClassType_lfno_unannClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#unannClassType_lfno_unannClassOrInterfaceType.
    def exitUnannClassType_lfno_unannClassOrInterfaceType(self, ctx:Java8Parser.UnannClassType_lfno_unannClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#unannInterfaceType.
    def enterUnannInterfaceType(self, ctx:Java8Parser.UnannInterfaceTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#unannInterfaceType.
    def exitUnannInterfaceType(self, ctx:Java8Parser.UnannInterfaceTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#unannInterfaceType_lf_unannClassOrInterfaceType.
    def enterUnannInterfaceType_lf_unannClassOrInterfaceType(self, ctx:Java8Parser.UnannInterfaceType_lf_unannClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#unannInterfaceType_lf_unannClassOrInterfaceType.
    def exitUnannInterfaceType_lf_unannClassOrInterfaceType(self, ctx:Java8Parser.UnannInterfaceType_lf_unannClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#unannInterfaceType_lfno_unannClassOrInterfaceType.
    def enterUnannInterfaceType_lfno_unannClassOrInterfaceType(self, ctx:Java8Parser.UnannInterfaceType_lfno_unannClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#unannInterfaceType_lfno_unannClassOrInterfaceType.
    def exitUnannInterfaceType_lfno_unannClassOrInterfaceType(self, ctx:Java8Parser.UnannInterfaceType_lfno_unannClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#unannTypeVariable.
    def enterUnannTypeVariable(self, ctx:Java8Parser.UnannTypeVariableContext):
        pass

    # Exit a parse tree produced by Java8Parser#unannTypeVariable.
    def exitUnannTypeVariable(self, ctx:Java8Parser.UnannTypeVariableContext):
        pass


    # Enter a parse tree produced by Java8Parser#unannArrayType.
    def enterUnannArrayType(self, ctx:Java8Parser.UnannArrayTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#unannArrayType.
    def exitUnannArrayType(self, ctx:Java8Parser.UnannArrayTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:Java8Parser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:Java8Parser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#methodModifier.
    def enterMethodModifier(self, ctx:Java8Parser.MethodModifierContext):
        pass

    # Exit a parse tree produced by Java8Parser#methodModifier.
    def exitMethodModifier(self, ctx:Java8Parser.MethodModifierContext):
        pass


    # Enter a parse tree produced by Java8Parser#methodHeader.
    def enterMethodHeader(self, ctx:Java8Parser.MethodHeaderContext):
        pass

    # Exit a parse tree produced by Java8Parser#methodHeader.
    def exitMethodHeader(self, ctx:Java8Parser.MethodHeaderContext):
        pass


    # Enter a parse tree produced by Java8Parser#result.
    def enterResult(self, ctx:Java8Parser.ResultContext):
        pass

    # Exit a parse tree produced by Java8Parser#result.
    def exitResult(self, ctx:Java8Parser.ResultContext):
        pass


    # Enter a parse tree produced by Java8Parser#methodDeclarator.
    def enterMethodDeclarator(self, ctx:Java8Parser.MethodDeclaratorContext):
        pass

    # Exit a parse tree produced by Java8Parser#methodDeclarator.
    def exitMethodDeclarator(self, ctx:Java8Parser.MethodDeclaratorContext):
        pass


    # Enter a parse tree produced by Java8Parser#formalParameterList.
    def enterFormalParameterList(self, ctx:Java8Parser.FormalParameterListContext):
        pass

    # Exit a parse tree produced by Java8Parser#formalParameterList.
    def exitFormalParameterList(self, ctx:Java8Parser.FormalParameterListContext):
        pass


    # Enter a parse tree produced by Java8Parser#formalParameters.
    def enterFormalParameters(self, ctx:Java8Parser.FormalParametersContext):
        pass

    # Exit a parse tree produced by Java8Parser#formalParameters.
    def exitFormalParameters(self, ctx:Java8Parser.FormalParametersContext):
        pass


    # Enter a parse tree produced by Java8Parser#formalParameter.
    def enterFormalParameter(self, ctx:Java8Parser.FormalParameterContext):
        pass

    # Exit a parse tree produced by Java8Parser#formalParameter.
    def exitFormalParameter(self, ctx:Java8Parser.FormalParameterContext):
        pass


    # Enter a parse tree produced by Java8Parser#variableModifier.
    def enterVariableModifier(self, ctx:Java8Parser.VariableModifierContext):
        pass

    # Exit a parse tree produced by Java8Parser#variableModifier.
    def exitVariableModifier(self, ctx:Java8Parser.VariableModifierContext):
        pass


    # Enter a parse tree produced by Java8Parser#lastFormalParameter.
    def enterLastFormalParameter(self, ctx:Java8Parser.LastFormalParameterContext):
        pass

    # Exit a parse tree produced by Java8Parser#lastFormalParameter.
    def exitLastFormalParameter(self, ctx:Java8Parser.LastFormalParameterContext):
        pass


    # Enter a parse tree produced by Java8Parser#receiverParameter.
    def enterReceiverParameter(self, ctx:Java8Parser.ReceiverParameterContext):
        pass

    # Exit a parse tree produced by Java8Parser#receiverParameter.
    def exitReceiverParameter(self, ctx:Java8Parser.ReceiverParameterContext):
        pass


    # Enter a parse tree produced by Java8Parser#throws_.
    def enterThrows_(self, ctx:Java8Parser.Throws_Context):
        pass

    # Exit a parse tree produced by Java8Parser#throws_.
    def exitThrows_(self, ctx:Java8Parser.Throws_Context):
        pass


    # Enter a parse tree produced by Java8Parser#exceptionTypeList.
    def enterExceptionTypeList(self, ctx:Java8Parser.ExceptionTypeListContext):
        pass

    # Exit a parse tree produced by Java8Parser#exceptionTypeList.
    def exitExceptionTypeList(self, ctx:Java8Parser.ExceptionTypeListContext):
        pass


    # Enter a parse tree produced by Java8Parser#exceptionType.
    def enterExceptionType(self, ctx:Java8Parser.ExceptionTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#exceptionType.
    def exitExceptionType(self, ctx:Java8Parser.ExceptionTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#methodBody.
    def enterMethodBody(self, ctx:Java8Parser.MethodBodyContext):
        pass

    # Exit a parse tree produced by Java8Parser#methodBody.
    def exitMethodBody(self, ctx:Java8Parser.MethodBodyContext):
        pass


    # Enter a parse tree produced by Java8Parser#instanceInitializer.
    def enterInstanceInitializer(self, ctx:Java8Parser.InstanceInitializerContext):
        pass

    # Exit a parse tree produced by Java8Parser#instanceInitializer.
    def exitInstanceInitializer(self, ctx:Java8Parser.InstanceInitializerContext):
        pass


    # Enter a parse tree produced by Java8Parser#staticInitializer.
    def enterStaticInitializer(self, ctx:Java8Parser.StaticInitializerContext):
        pass

    # Exit a parse tree produced by Java8Parser#staticInitializer.
    def exitStaticInitializer(self, ctx:Java8Parser.StaticInitializerContext):
        pass


    # Enter a parse tree produced by Java8Parser#constructorDeclaration.
    def enterConstructorDeclaration(self, ctx:Java8Parser.ConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#constructorDeclaration.
    def exitConstructorDeclaration(self, ctx:Java8Parser.ConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#constructorModifier.
    def enterConstructorModifier(self, ctx:Java8Parser.ConstructorModifierContext):
        pass

    # Exit a parse tree produced by Java8Parser#constructorModifier.
    def exitConstructorModifier(self, ctx:Java8Parser.ConstructorModifierContext):
        pass


    # Enter a parse tree produced by Java8Parser#constructorDeclarator.
    def enterConstructorDeclarator(self, ctx:Java8Parser.ConstructorDeclaratorContext):
        pass

    # Exit a parse tree produced by Java8Parser#constructorDeclarator.
    def exitConstructorDeclarator(self, ctx:Java8Parser.ConstructorDeclaratorContext):
        pass


    # Enter a parse tree produced by Java8Parser#simpleTypeName.
    def enterSimpleTypeName(self, ctx:Java8Parser.SimpleTypeNameContext):
        pass

    # Exit a parse tree produced by Java8Parser#simpleTypeName.
    def exitSimpleTypeName(self, ctx:Java8Parser.SimpleTypeNameContext):
        pass


    # Enter a parse tree produced by Java8Parser#constructorBody.
    def enterConstructorBody(self, ctx:Java8Parser.ConstructorBodyContext):
        pass

    # Exit a parse tree produced by Java8Parser#constructorBody.
    def exitConstructorBody(self, ctx:Java8Parser.ConstructorBodyContext):
        pass


    # Enter a parse tree produced by Java8Parser#explicitConstructorInvocation.
    def enterExplicitConstructorInvocation(self, ctx:Java8Parser.ExplicitConstructorInvocationContext):
        pass

    # Exit a parse tree produced by Java8Parser#explicitConstructorInvocation.
    def exitExplicitConstructorInvocation(self, ctx:Java8Parser.ExplicitConstructorInvocationContext):
        pass


    # Enter a parse tree produced by Java8Parser#enumDeclaration.
    def enterEnumDeclaration(self, ctx:Java8Parser.EnumDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#enumDeclaration.
    def exitEnumDeclaration(self, ctx:Java8Parser.EnumDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#enumBody.
    def enterEnumBody(self, ctx:Java8Parser.EnumBodyContext):
        pass

    # Exit a parse tree produced by Java8Parser#enumBody.
    def exitEnumBody(self, ctx:Java8Parser.EnumBodyContext):
        pass


    # Enter a parse tree produced by Java8Parser#enumConstantList.
    def enterEnumConstantList(self, ctx:Java8Parser.EnumConstantListContext):
        pass

    # Exit a parse tree produced by Java8Parser#enumConstantList.
    def exitEnumConstantList(self, ctx:Java8Parser.EnumConstantListContext):
        pass


    # Enter a parse tree produced by Java8Parser#enumConstant.
    def enterEnumConstant(self, ctx:Java8Parser.EnumConstantContext):
        pass

    # Exit a parse tree produced by Java8Parser#enumConstant.
    def exitEnumConstant(self, ctx:Java8Parser.EnumConstantContext):
        pass


    # Enter a parse tree produced by Java8Parser#enumConstantModifier.
    def enterEnumConstantModifier(self, ctx:Java8Parser.EnumConstantModifierContext):
        pass

    # Exit a parse tree produced by Java8Parser#enumConstantModifier.
    def exitEnumConstantModifier(self, ctx:Java8Parser.EnumConstantModifierContext):
        pass


    # Enter a parse tree produced by Java8Parser#enumBodyDeclarations.
    def enterEnumBodyDeclarations(self, ctx:Java8Parser.EnumBodyDeclarationsContext):
        pass

    # Exit a parse tree produced by Java8Parser#enumBodyDeclarations.
    def exitEnumBodyDeclarations(self, ctx:Java8Parser.EnumBodyDeclarationsContext):
        pass


    # Enter a parse tree produced by Java8Parser#interfaceDeclaration.
    def enterInterfaceDeclaration(self, ctx:Java8Parser.InterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#interfaceDeclaration.
    def exitInterfaceDeclaration(self, ctx:Java8Parser.InterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#normalInterfaceDeclaration.
    def enterNormalInterfaceDeclaration(self, ctx:Java8Parser.NormalInterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#normalInterfaceDeclaration.
    def exitNormalInterfaceDeclaration(self, ctx:Java8Parser.NormalInterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#interfaceModifier.
    def enterInterfaceModifier(self, ctx:Java8Parser.InterfaceModifierContext):
        pass

    # Exit a parse tree produced by Java8Parser#interfaceModifier.
    def exitInterfaceModifier(self, ctx:Java8Parser.InterfaceModifierContext):
        pass


    # Enter a parse tree produced by Java8Parser#extendsInterfaces.
    def enterExtendsInterfaces(self, ctx:Java8Parser.ExtendsInterfacesContext):
        pass

    # Exit a parse tree produced by Java8Parser#extendsInterfaces.
    def exitExtendsInterfaces(self, ctx:Java8Parser.ExtendsInterfacesContext):
        pass


    # Enter a parse tree produced by Java8Parser#interfaceBody.
    def enterInterfaceBody(self, ctx:Java8Parser.InterfaceBodyContext):
        pass

    # Exit a parse tree produced by Java8Parser#interfaceBody.
    def exitInterfaceBody(self, ctx:Java8Parser.InterfaceBodyContext):
        pass


    # Enter a parse tree produced by Java8Parser#interfaceMemberDeclaration.
    def enterInterfaceMemberDeclaration(self, ctx:Java8Parser.InterfaceMemberDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#interfaceMemberDeclaration.
    def exitInterfaceMemberDeclaration(self, ctx:Java8Parser.InterfaceMemberDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#constantDeclaration.
    def enterConstantDeclaration(self, ctx:Java8Parser.ConstantDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#constantDeclaration.
    def exitConstantDeclaration(self, ctx:Java8Parser.ConstantDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#constantModifier.
    def enterConstantModifier(self, ctx:Java8Parser.ConstantModifierContext):
        pass

    # Exit a parse tree produced by Java8Parser#constantModifier.
    def exitConstantModifier(self, ctx:Java8Parser.ConstantModifierContext):
        pass


    # Enter a parse tree produced by Java8Parser#interfaceMethodDeclaration.
    def enterInterfaceMethodDeclaration(self, ctx:Java8Parser.InterfaceMethodDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#interfaceMethodDeclaration.
    def exitInterfaceMethodDeclaration(self, ctx:Java8Parser.InterfaceMethodDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#interfaceMethodModifier.
    def enterInterfaceMethodModifier(self, ctx:Java8Parser.InterfaceMethodModifierContext):
        pass

    # Exit a parse tree produced by Java8Parser#interfaceMethodModifier.
    def exitInterfaceMethodModifier(self, ctx:Java8Parser.InterfaceMethodModifierContext):
        pass


    # Enter a parse tree produced by Java8Parser#annotationTypeDeclaration.
    def enterAnnotationTypeDeclaration(self, ctx:Java8Parser.AnnotationTypeDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#annotationTypeDeclaration.
    def exitAnnotationTypeDeclaration(self, ctx:Java8Parser.AnnotationTypeDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#annotationTypeBody.
    def enterAnnotationTypeBody(self, ctx:Java8Parser.AnnotationTypeBodyContext):
        pass

    # Exit a parse tree produced by Java8Parser#annotationTypeBody.
    def exitAnnotationTypeBody(self, ctx:Java8Parser.AnnotationTypeBodyContext):
        pass


    # Enter a parse tree produced by Java8Parser#annotationTypeMemberDeclaration.
    def enterAnnotationTypeMemberDeclaration(self, ctx:Java8Parser.AnnotationTypeMemberDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#annotationTypeMemberDeclaration.
    def exitAnnotationTypeMemberDeclaration(self, ctx:Java8Parser.AnnotationTypeMemberDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#annotationTypeElementDeclaration.
    def enterAnnotationTypeElementDeclaration(self, ctx:Java8Parser.AnnotationTypeElementDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#annotationTypeElementDeclaration.
    def exitAnnotationTypeElementDeclaration(self, ctx:Java8Parser.AnnotationTypeElementDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#annotationTypeElementModifier.
    def enterAnnotationTypeElementModifier(self, ctx:Java8Parser.AnnotationTypeElementModifierContext):
        pass

    # Exit a parse tree produced by Java8Parser#annotationTypeElementModifier.
    def exitAnnotationTypeElementModifier(self, ctx:Java8Parser.AnnotationTypeElementModifierContext):
        pass


    # Enter a parse tree produced by Java8Parser#defaultValue.
    def enterDefaultValue(self, ctx:Java8Parser.DefaultValueContext):
        pass

    # Exit a parse tree produced by Java8Parser#defaultValue.
    def exitDefaultValue(self, ctx:Java8Parser.DefaultValueContext):
        pass


    # Enter a parse tree produced by Java8Parser#annotation.
    def enterAnnotation(self, ctx:Java8Parser.AnnotationContext):
        pass

    # Exit a parse tree produced by Java8Parser#annotation.
    def exitAnnotation(self, ctx:Java8Parser.AnnotationContext):
        pass


    # Enter a parse tree produced by Java8Parser#normalAnnotation.
    def enterNormalAnnotation(self, ctx:Java8Parser.NormalAnnotationContext):
        pass

    # Exit a parse tree produced by Java8Parser#normalAnnotation.
    def exitNormalAnnotation(self, ctx:Java8Parser.NormalAnnotationContext):
        pass


    # Enter a parse tree produced by Java8Parser#elementValuePairList.
    def enterElementValuePairList(self, ctx:Java8Parser.ElementValuePairListContext):
        pass

    # Exit a parse tree produced by Java8Parser#elementValuePairList.
    def exitElementValuePairList(self, ctx:Java8Parser.ElementValuePairListContext):
        pass


    # Enter a parse tree produced by Java8Parser#elementValuePair.
    def enterElementValuePair(self, ctx:Java8Parser.ElementValuePairContext):
        pass

    # Exit a parse tree produced by Java8Parser#elementValuePair.
    def exitElementValuePair(self, ctx:Java8Parser.ElementValuePairContext):
        pass


    # Enter a parse tree produced by Java8Parser#elementValue.
    def enterElementValue(self, ctx:Java8Parser.ElementValueContext):
        pass

    # Exit a parse tree produced by Java8Parser#elementValue.
    def exitElementValue(self, ctx:Java8Parser.ElementValueContext):
        pass


    # Enter a parse tree produced by Java8Parser#elementValueArrayInitializer.
    def enterElementValueArrayInitializer(self, ctx:Java8Parser.ElementValueArrayInitializerContext):
        pass

    # Exit a parse tree produced by Java8Parser#elementValueArrayInitializer.
    def exitElementValueArrayInitializer(self, ctx:Java8Parser.ElementValueArrayInitializerContext):
        pass


    # Enter a parse tree produced by Java8Parser#elementValueList.
    def enterElementValueList(self, ctx:Java8Parser.ElementValueListContext):
        pass

    # Exit a parse tree produced by Java8Parser#elementValueList.
    def exitElementValueList(self, ctx:Java8Parser.ElementValueListContext):
        pass


    # Enter a parse tree produced by Java8Parser#markerAnnotation.
    def enterMarkerAnnotation(self, ctx:Java8Parser.MarkerAnnotationContext):
        pass

    # Exit a parse tree produced by Java8Parser#markerAnnotation.
    def exitMarkerAnnotation(self, ctx:Java8Parser.MarkerAnnotationContext):
        pass


    # Enter a parse tree produced by Java8Parser#singleElementAnnotation.
    def enterSingleElementAnnotation(self, ctx:Java8Parser.SingleElementAnnotationContext):
        pass

    # Exit a parse tree produced by Java8Parser#singleElementAnnotation.
    def exitSingleElementAnnotation(self, ctx:Java8Parser.SingleElementAnnotationContext):
        pass


    # Enter a parse tree produced by Java8Parser#arrayInitializer.
    def enterArrayInitializer(self, ctx:Java8Parser.ArrayInitializerContext):
        pass

    # Exit a parse tree produced by Java8Parser#arrayInitializer.
    def exitArrayInitializer(self, ctx:Java8Parser.ArrayInitializerContext):
        pass


    # Enter a parse tree produced by Java8Parser#variableInitializerList.
    def enterVariableInitializerList(self, ctx:Java8Parser.VariableInitializerListContext):
        pass

    # Exit a parse tree produced by Java8Parser#variableInitializerList.
    def exitVariableInitializerList(self, ctx:Java8Parser.VariableInitializerListContext):
        pass


    # Enter a parse tree produced by Java8Parser#block.
    def enterBlock(self, ctx:Java8Parser.BlockContext):
        pass

    # Exit a parse tree produced by Java8Parser#block.
    def exitBlock(self, ctx:Java8Parser.BlockContext):
        pass


    # Enter a parse tree produced by Java8Parser#blockStatements.
    def enterBlockStatements(self, ctx:Java8Parser.BlockStatementsContext):
        pass

    # Exit a parse tree produced by Java8Parser#blockStatements.
    def exitBlockStatements(self, ctx:Java8Parser.BlockStatementsContext):
        pass


    # Enter a parse tree produced by Java8Parser#blockStatement.
    def enterBlockStatement(self, ctx:Java8Parser.BlockStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#blockStatement.
    def exitBlockStatement(self, ctx:Java8Parser.BlockStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#localVariableDeclarationStatement.
    def enterLocalVariableDeclarationStatement(self, ctx:Java8Parser.LocalVariableDeclarationStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#localVariableDeclarationStatement.
    def exitLocalVariableDeclarationStatement(self, ctx:Java8Parser.LocalVariableDeclarationStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#localVariableDeclaration.
    def enterLocalVariableDeclaration(self, ctx:Java8Parser.LocalVariableDeclarationContext):
        pass

    # Exit a parse tree produced by Java8Parser#localVariableDeclaration.
    def exitLocalVariableDeclaration(self, ctx:Java8Parser.LocalVariableDeclarationContext):
        pass


    # Enter a parse tree produced by Java8Parser#statement.
    def enterStatement(self, ctx:Java8Parser.StatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#statement.
    def exitStatement(self, ctx:Java8Parser.StatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#statementNoShortIf.
    def enterStatementNoShortIf(self, ctx:Java8Parser.StatementNoShortIfContext):
        pass

    # Exit a parse tree produced by Java8Parser#statementNoShortIf.
    def exitStatementNoShortIf(self, ctx:Java8Parser.StatementNoShortIfContext):
        pass


    # Enter a parse tree produced by Java8Parser#statementWithoutTrailingSubstatement.
    def enterStatementWithoutTrailingSubstatement(self, ctx:Java8Parser.StatementWithoutTrailingSubstatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#statementWithoutTrailingSubstatement.
    def exitStatementWithoutTrailingSubstatement(self, ctx:Java8Parser.StatementWithoutTrailingSubstatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#emptyStatement.
    def enterEmptyStatement(self, ctx:Java8Parser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#emptyStatement.
    def exitEmptyStatement(self, ctx:Java8Parser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#labeledStatement.
    def enterLabeledStatement(self, ctx:Java8Parser.LabeledStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#labeledStatement.
    def exitLabeledStatement(self, ctx:Java8Parser.LabeledStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#labeledStatementNoShortIf.
    def enterLabeledStatementNoShortIf(self, ctx:Java8Parser.LabeledStatementNoShortIfContext):
        pass

    # Exit a parse tree produced by Java8Parser#labeledStatementNoShortIf.
    def exitLabeledStatementNoShortIf(self, ctx:Java8Parser.LabeledStatementNoShortIfContext):
        pass


    # Enter a parse tree produced by Java8Parser#expressionStatement.
    def enterExpressionStatement(self, ctx:Java8Parser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#expressionStatement.
    def exitExpressionStatement(self, ctx:Java8Parser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#statementExpression.
    def enterStatementExpression(self, ctx:Java8Parser.StatementExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#statementExpression.
    def exitStatementExpression(self, ctx:Java8Parser.StatementExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#ifThenStatement.
    def enterIfThenStatement(self, ctx:Java8Parser.IfThenStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#ifThenStatement.
    def exitIfThenStatement(self, ctx:Java8Parser.IfThenStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#ifThenElseStatement.
    def enterIfThenElseStatement(self, ctx:Java8Parser.IfThenElseStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#ifThenElseStatement.
    def exitIfThenElseStatement(self, ctx:Java8Parser.IfThenElseStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#ifThenElseStatementNoShortIf.
    def enterIfThenElseStatementNoShortIf(self, ctx:Java8Parser.IfThenElseStatementNoShortIfContext):
        pass

    # Exit a parse tree produced by Java8Parser#ifThenElseStatementNoShortIf.
    def exitIfThenElseStatementNoShortIf(self, ctx:Java8Parser.IfThenElseStatementNoShortIfContext):
        pass


    # Enter a parse tree produced by Java8Parser#assertStatement.
    def enterAssertStatement(self, ctx:Java8Parser.AssertStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#assertStatement.
    def exitAssertStatement(self, ctx:Java8Parser.AssertStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#switchStatement.
    def enterSwitchStatement(self, ctx:Java8Parser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#switchStatement.
    def exitSwitchStatement(self, ctx:Java8Parser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#switchBlock.
    def enterSwitchBlock(self, ctx:Java8Parser.SwitchBlockContext):
        pass

    # Exit a parse tree produced by Java8Parser#switchBlock.
    def exitSwitchBlock(self, ctx:Java8Parser.SwitchBlockContext):
        pass


    # Enter a parse tree produced by Java8Parser#switchBlockStatementGroup.
    def enterSwitchBlockStatementGroup(self, ctx:Java8Parser.SwitchBlockStatementGroupContext):
        pass

    # Exit a parse tree produced by Java8Parser#switchBlockStatementGroup.
    def exitSwitchBlockStatementGroup(self, ctx:Java8Parser.SwitchBlockStatementGroupContext):
        pass


    # Enter a parse tree produced by Java8Parser#switchLabels.
    def enterSwitchLabels(self, ctx:Java8Parser.SwitchLabelsContext):
        pass

    # Exit a parse tree produced by Java8Parser#switchLabels.
    def exitSwitchLabels(self, ctx:Java8Parser.SwitchLabelsContext):
        pass


    # Enter a parse tree produced by Java8Parser#switchLabel.
    def enterSwitchLabel(self, ctx:Java8Parser.SwitchLabelContext):
        pass

    # Exit a parse tree produced by Java8Parser#switchLabel.
    def exitSwitchLabel(self, ctx:Java8Parser.SwitchLabelContext):
        pass


    # Enter a parse tree produced by Java8Parser#enumConstantName.
    def enterEnumConstantName(self, ctx:Java8Parser.EnumConstantNameContext):
        pass

    # Exit a parse tree produced by Java8Parser#enumConstantName.
    def exitEnumConstantName(self, ctx:Java8Parser.EnumConstantNameContext):
        pass


    # Enter a parse tree produced by Java8Parser#whileStatement.
    def enterWhileStatement(self, ctx:Java8Parser.WhileStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#whileStatement.
    def exitWhileStatement(self, ctx:Java8Parser.WhileStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#whileStatementNoShortIf.
    def enterWhileStatementNoShortIf(self, ctx:Java8Parser.WhileStatementNoShortIfContext):
        pass

    # Exit a parse tree produced by Java8Parser#whileStatementNoShortIf.
    def exitWhileStatementNoShortIf(self, ctx:Java8Parser.WhileStatementNoShortIfContext):
        pass


    # Enter a parse tree produced by Java8Parser#doStatement.
    def enterDoStatement(self, ctx:Java8Parser.DoStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#doStatement.
    def exitDoStatement(self, ctx:Java8Parser.DoStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#forStatement.
    def enterForStatement(self, ctx:Java8Parser.ForStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#forStatement.
    def exitForStatement(self, ctx:Java8Parser.ForStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#forStatementNoShortIf.
    def enterForStatementNoShortIf(self, ctx:Java8Parser.ForStatementNoShortIfContext):
        pass

    # Exit a parse tree produced by Java8Parser#forStatementNoShortIf.
    def exitForStatementNoShortIf(self, ctx:Java8Parser.ForStatementNoShortIfContext):
        pass


    # Enter a parse tree produced by Java8Parser#basicForStatement.
    def enterBasicForStatement(self, ctx:Java8Parser.BasicForStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#basicForStatement.
    def exitBasicForStatement(self, ctx:Java8Parser.BasicForStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#basicForStatementNoShortIf.
    def enterBasicForStatementNoShortIf(self, ctx:Java8Parser.BasicForStatementNoShortIfContext):
        pass

    # Exit a parse tree produced by Java8Parser#basicForStatementNoShortIf.
    def exitBasicForStatementNoShortIf(self, ctx:Java8Parser.BasicForStatementNoShortIfContext):
        pass


    # Enter a parse tree produced by Java8Parser#forInit.
    def enterForInit(self, ctx:Java8Parser.ForInitContext):
        pass

    # Exit a parse tree produced by Java8Parser#forInit.
    def exitForInit(self, ctx:Java8Parser.ForInitContext):
        pass


    # Enter a parse tree produced by Java8Parser#forUpdate.
    def enterForUpdate(self, ctx:Java8Parser.ForUpdateContext):
        pass

    # Exit a parse tree produced by Java8Parser#forUpdate.
    def exitForUpdate(self, ctx:Java8Parser.ForUpdateContext):
        pass


    # Enter a parse tree produced by Java8Parser#statementExpressionList.
    def enterStatementExpressionList(self, ctx:Java8Parser.StatementExpressionListContext):
        pass

    # Exit a parse tree produced by Java8Parser#statementExpressionList.
    def exitStatementExpressionList(self, ctx:Java8Parser.StatementExpressionListContext):
        pass


    # Enter a parse tree produced by Java8Parser#enhancedForStatement.
    def enterEnhancedForStatement(self, ctx:Java8Parser.EnhancedForStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#enhancedForStatement.
    def exitEnhancedForStatement(self, ctx:Java8Parser.EnhancedForStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#enhancedForStatementNoShortIf.
    def enterEnhancedForStatementNoShortIf(self, ctx:Java8Parser.EnhancedForStatementNoShortIfContext):
        pass

    # Exit a parse tree produced by Java8Parser#enhancedForStatementNoShortIf.
    def exitEnhancedForStatementNoShortIf(self, ctx:Java8Parser.EnhancedForStatementNoShortIfContext):
        pass


    # Enter a parse tree produced by Java8Parser#breakStatement.
    def enterBreakStatement(self, ctx:Java8Parser.BreakStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#breakStatement.
    def exitBreakStatement(self, ctx:Java8Parser.BreakStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#continueStatement.
    def enterContinueStatement(self, ctx:Java8Parser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#continueStatement.
    def exitContinueStatement(self, ctx:Java8Parser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#returnStatement.
    def enterReturnStatement(self, ctx:Java8Parser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#returnStatement.
    def exitReturnStatement(self, ctx:Java8Parser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#throwStatement.
    def enterThrowStatement(self, ctx:Java8Parser.ThrowStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#throwStatement.
    def exitThrowStatement(self, ctx:Java8Parser.ThrowStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#synchronizedStatement.
    def enterSynchronizedStatement(self, ctx:Java8Parser.SynchronizedStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#synchronizedStatement.
    def exitSynchronizedStatement(self, ctx:Java8Parser.SynchronizedStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#tryStatement.
    def enterTryStatement(self, ctx:Java8Parser.TryStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#tryStatement.
    def exitTryStatement(self, ctx:Java8Parser.TryStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#catches.
    def enterCatches(self, ctx:Java8Parser.CatchesContext):
        pass

    # Exit a parse tree produced by Java8Parser#catches.
    def exitCatches(self, ctx:Java8Parser.CatchesContext):
        pass


    # Enter a parse tree produced by Java8Parser#catchClause.
    def enterCatchClause(self, ctx:Java8Parser.CatchClauseContext):
        pass

    # Exit a parse tree produced by Java8Parser#catchClause.
    def exitCatchClause(self, ctx:Java8Parser.CatchClauseContext):
        pass


    # Enter a parse tree produced by Java8Parser#catchFormalParameter.
    def enterCatchFormalParameter(self, ctx:Java8Parser.CatchFormalParameterContext):
        pass

    # Exit a parse tree produced by Java8Parser#catchFormalParameter.
    def exitCatchFormalParameter(self, ctx:Java8Parser.CatchFormalParameterContext):
        pass


    # Enter a parse tree produced by Java8Parser#catchType.
    def enterCatchType(self, ctx:Java8Parser.CatchTypeContext):
        pass

    # Exit a parse tree produced by Java8Parser#catchType.
    def exitCatchType(self, ctx:Java8Parser.CatchTypeContext):
        pass


    # Enter a parse tree produced by Java8Parser#finally_.
    def enterFinally_(self, ctx:Java8Parser.Finally_Context):
        pass

    # Exit a parse tree produced by Java8Parser#finally_.
    def exitFinally_(self, ctx:Java8Parser.Finally_Context):
        pass


    # Enter a parse tree produced by Java8Parser#tryWithResourcesStatement.
    def enterTryWithResourcesStatement(self, ctx:Java8Parser.TryWithResourcesStatementContext):
        pass

    # Exit a parse tree produced by Java8Parser#tryWithResourcesStatement.
    def exitTryWithResourcesStatement(self, ctx:Java8Parser.TryWithResourcesStatementContext):
        pass


    # Enter a parse tree produced by Java8Parser#resourceSpecification.
    def enterResourceSpecification(self, ctx:Java8Parser.ResourceSpecificationContext):
        pass

    # Exit a parse tree produced by Java8Parser#resourceSpecification.
    def exitResourceSpecification(self, ctx:Java8Parser.ResourceSpecificationContext):
        pass


    # Enter a parse tree produced by Java8Parser#resourceList.
    def enterResourceList(self, ctx:Java8Parser.ResourceListContext):
        pass

    # Exit a parse tree produced by Java8Parser#resourceList.
    def exitResourceList(self, ctx:Java8Parser.ResourceListContext):
        pass


    # Enter a parse tree produced by Java8Parser#resource.
    def enterResource(self, ctx:Java8Parser.ResourceContext):
        pass

    # Exit a parse tree produced by Java8Parser#resource.
    def exitResource(self, ctx:Java8Parser.ResourceContext):
        pass


    # Enter a parse tree produced by Java8Parser#primary.
    def enterPrimary(self, ctx:Java8Parser.PrimaryContext):
        pass

    # Exit a parse tree produced by Java8Parser#primary.
    def exitPrimary(self, ctx:Java8Parser.PrimaryContext):
        pass


    # Enter a parse tree produced by Java8Parser#primaryNoNewArray.
    def enterPrimaryNoNewArray(self, ctx:Java8Parser.PrimaryNoNewArrayContext):
        pass

    # Exit a parse tree produced by Java8Parser#primaryNoNewArray.
    def exitPrimaryNoNewArray(self, ctx:Java8Parser.PrimaryNoNewArrayContext):
        pass


    # Enter a parse tree produced by Java8Parser#primaryNoNewArray_lf_arrayAccess.
    def enterPrimaryNoNewArray_lf_arrayAccess(self, ctx:Java8Parser.PrimaryNoNewArray_lf_arrayAccessContext):
        pass

    # Exit a parse tree produced by Java8Parser#primaryNoNewArray_lf_arrayAccess.
    def exitPrimaryNoNewArray_lf_arrayAccess(self, ctx:Java8Parser.PrimaryNoNewArray_lf_arrayAccessContext):
        pass


    # Enter a parse tree produced by Java8Parser#primaryNoNewArray_lfno_arrayAccess.
    def enterPrimaryNoNewArray_lfno_arrayAccess(self, ctx:Java8Parser.PrimaryNoNewArray_lfno_arrayAccessContext):
        pass

    # Exit a parse tree produced by Java8Parser#primaryNoNewArray_lfno_arrayAccess.
    def exitPrimaryNoNewArray_lfno_arrayAccess(self, ctx:Java8Parser.PrimaryNoNewArray_lfno_arrayAccessContext):
        pass


    # Enter a parse tree produced by Java8Parser#primaryNoNewArray_lf_primary.
    def enterPrimaryNoNewArray_lf_primary(self, ctx:Java8Parser.PrimaryNoNewArray_lf_primaryContext):
        pass

    # Exit a parse tree produced by Java8Parser#primaryNoNewArray_lf_primary.
    def exitPrimaryNoNewArray_lf_primary(self, ctx:Java8Parser.PrimaryNoNewArray_lf_primaryContext):
        pass


    # Enter a parse tree produced by Java8Parser#primaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary.
    def enterPrimaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary(self, ctx:Java8Parser.PrimaryNoNewArray_lf_primary_lf_arrayAccess_lf_primaryContext):
        pass

    # Exit a parse tree produced by Java8Parser#primaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary.
    def exitPrimaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary(self, ctx:Java8Parser.PrimaryNoNewArray_lf_primary_lf_arrayAccess_lf_primaryContext):
        pass


    # Enter a parse tree produced by Java8Parser#primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary.
    def enterPrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary(self, ctx:Java8Parser.PrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primaryContext):
        pass

    # Exit a parse tree produced by Java8Parser#primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary.
    def exitPrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary(self, ctx:Java8Parser.PrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primaryContext):
        pass


    # Enter a parse tree produced by Java8Parser#primaryNoNewArray_lfno_primary.
    def enterPrimaryNoNewArray_lfno_primary(self, ctx:Java8Parser.PrimaryNoNewArray_lfno_primaryContext):
        pass

    # Exit a parse tree produced by Java8Parser#primaryNoNewArray_lfno_primary.
    def exitPrimaryNoNewArray_lfno_primary(self, ctx:Java8Parser.PrimaryNoNewArray_lfno_primaryContext):
        pass


    # Enter a parse tree produced by Java8Parser#primaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary.
    def enterPrimaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary(self, ctx:Java8Parser.PrimaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primaryContext):
        pass

    # Exit a parse tree produced by Java8Parser#primaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary.
    def exitPrimaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary(self, ctx:Java8Parser.PrimaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primaryContext):
        pass


    # Enter a parse tree produced by Java8Parser#primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary.
    def enterPrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary(self, ctx:Java8Parser.PrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primaryContext):
        pass

    # Exit a parse tree produced by Java8Parser#primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary.
    def exitPrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary(self, ctx:Java8Parser.PrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primaryContext):
        pass


    # Enter a parse tree produced by Java8Parser#classInstanceCreationExpression.
    def enterClassInstanceCreationExpression(self, ctx:Java8Parser.ClassInstanceCreationExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#classInstanceCreationExpression.
    def exitClassInstanceCreationExpression(self, ctx:Java8Parser.ClassInstanceCreationExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#classInstanceCreationExpression_lf_primary.
    def enterClassInstanceCreationExpression_lf_primary(self, ctx:Java8Parser.ClassInstanceCreationExpression_lf_primaryContext):
        pass

    # Exit a parse tree produced by Java8Parser#classInstanceCreationExpression_lf_primary.
    def exitClassInstanceCreationExpression_lf_primary(self, ctx:Java8Parser.ClassInstanceCreationExpression_lf_primaryContext):
        pass


    # Enter a parse tree produced by Java8Parser#classInstanceCreationExpression_lfno_primary.
    def enterClassInstanceCreationExpression_lfno_primary(self, ctx:Java8Parser.ClassInstanceCreationExpression_lfno_primaryContext):
        pass

    # Exit a parse tree produced by Java8Parser#classInstanceCreationExpression_lfno_primary.
    def exitClassInstanceCreationExpression_lfno_primary(self, ctx:Java8Parser.ClassInstanceCreationExpression_lfno_primaryContext):
        pass


    # Enter a parse tree produced by Java8Parser#typeArgumentsOrDiamond.
    def enterTypeArgumentsOrDiamond(self, ctx:Java8Parser.TypeArgumentsOrDiamondContext):
        pass

    # Exit a parse tree produced by Java8Parser#typeArgumentsOrDiamond.
    def exitTypeArgumentsOrDiamond(self, ctx:Java8Parser.TypeArgumentsOrDiamondContext):
        pass


    # Enter a parse tree produced by Java8Parser#fieldAccess.
    def enterFieldAccess(self, ctx:Java8Parser.FieldAccessContext):
        pass

    # Exit a parse tree produced by Java8Parser#fieldAccess.
    def exitFieldAccess(self, ctx:Java8Parser.FieldAccessContext):
        pass


    # Enter a parse tree produced by Java8Parser#fieldAccess_lf_primary.
    def enterFieldAccess_lf_primary(self, ctx:Java8Parser.FieldAccess_lf_primaryContext):
        pass

    # Exit a parse tree produced by Java8Parser#fieldAccess_lf_primary.
    def exitFieldAccess_lf_primary(self, ctx:Java8Parser.FieldAccess_lf_primaryContext):
        pass


    # Enter a parse tree produced by Java8Parser#fieldAccess_lfno_primary.
    def enterFieldAccess_lfno_primary(self, ctx:Java8Parser.FieldAccess_lfno_primaryContext):
        pass

    # Exit a parse tree produced by Java8Parser#fieldAccess_lfno_primary.
    def exitFieldAccess_lfno_primary(self, ctx:Java8Parser.FieldAccess_lfno_primaryContext):
        pass


    # Enter a parse tree produced by Java8Parser#arrayAccess.
    def enterArrayAccess(self, ctx:Java8Parser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by Java8Parser#arrayAccess.
    def exitArrayAccess(self, ctx:Java8Parser.ArrayAccessContext):
        pass


    # Enter a parse tree produced by Java8Parser#arrayAccess_lf_primary.
    def enterArrayAccess_lf_primary(self, ctx:Java8Parser.ArrayAccess_lf_primaryContext):
        pass

    # Exit a parse tree produced by Java8Parser#arrayAccess_lf_primary.
    def exitArrayAccess_lf_primary(self, ctx:Java8Parser.ArrayAccess_lf_primaryContext):
        pass


    # Enter a parse tree produced by Java8Parser#arrayAccess_lfno_primary.
    def enterArrayAccess_lfno_primary(self, ctx:Java8Parser.ArrayAccess_lfno_primaryContext):
        pass

    # Exit a parse tree produced by Java8Parser#arrayAccess_lfno_primary.
    def exitArrayAccess_lfno_primary(self, ctx:Java8Parser.ArrayAccess_lfno_primaryContext):
        pass


    # Enter a parse tree produced by Java8Parser#methodInvocation.
    def enterMethodInvocation(self, ctx:Java8Parser.MethodInvocationContext):
        pass

    # Exit a parse tree produced by Java8Parser#methodInvocation.
    def exitMethodInvocation(self, ctx:Java8Parser.MethodInvocationContext):
        pass


    # Enter a parse tree produced by Java8Parser#methodInvocation_lf_primary.
    def enterMethodInvocation_lf_primary(self, ctx:Java8Parser.MethodInvocation_lf_primaryContext):
        pass

    # Exit a parse tree produced by Java8Parser#methodInvocation_lf_primary.
    def exitMethodInvocation_lf_primary(self, ctx:Java8Parser.MethodInvocation_lf_primaryContext):
        pass


    # Enter a parse tree produced by Java8Parser#methodInvocation_lfno_primary.
    def enterMethodInvocation_lfno_primary(self, ctx:Java8Parser.MethodInvocation_lfno_primaryContext):
        pass

    # Exit a parse tree produced by Java8Parser#methodInvocation_lfno_primary.
    def exitMethodInvocation_lfno_primary(self, ctx:Java8Parser.MethodInvocation_lfno_primaryContext):
        pass


    # Enter a parse tree produced by Java8Parser#argumentList.
    def enterArgumentList(self, ctx:Java8Parser.ArgumentListContext):
        pass

    # Exit a parse tree produced by Java8Parser#argumentList.
    def exitArgumentList(self, ctx:Java8Parser.ArgumentListContext):
        pass


    # Enter a parse tree produced by Java8Parser#methodReference.
    def enterMethodReference(self, ctx:Java8Parser.MethodReferenceContext):
        pass

    # Exit a parse tree produced by Java8Parser#methodReference.
    def exitMethodReference(self, ctx:Java8Parser.MethodReferenceContext):
        pass


    # Enter a parse tree produced by Java8Parser#methodReference_lf_primary.
    def enterMethodReference_lf_primary(self, ctx:Java8Parser.MethodReference_lf_primaryContext):
        pass

    # Exit a parse tree produced by Java8Parser#methodReference_lf_primary.
    def exitMethodReference_lf_primary(self, ctx:Java8Parser.MethodReference_lf_primaryContext):
        pass


    # Enter a parse tree produced by Java8Parser#methodReference_lfno_primary.
    def enterMethodReference_lfno_primary(self, ctx:Java8Parser.MethodReference_lfno_primaryContext):
        pass

    # Exit a parse tree produced by Java8Parser#methodReference_lfno_primary.
    def exitMethodReference_lfno_primary(self, ctx:Java8Parser.MethodReference_lfno_primaryContext):
        pass


    # Enter a parse tree produced by Java8Parser#arrayCreationExpression.
    def enterArrayCreationExpression(self, ctx:Java8Parser.ArrayCreationExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#arrayCreationExpression.
    def exitArrayCreationExpression(self, ctx:Java8Parser.ArrayCreationExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#dimExprs.
    def enterDimExprs(self, ctx:Java8Parser.DimExprsContext):
        pass

    # Exit a parse tree produced by Java8Parser#dimExprs.
    def exitDimExprs(self, ctx:Java8Parser.DimExprsContext):
        pass


    # Enter a parse tree produced by Java8Parser#dimExpr.
    def enterDimExpr(self, ctx:Java8Parser.DimExprContext):
        pass

    # Exit a parse tree produced by Java8Parser#dimExpr.
    def exitDimExpr(self, ctx:Java8Parser.DimExprContext):
        pass


    # Enter a parse tree produced by Java8Parser#constantExpression.
    def enterConstantExpression(self, ctx:Java8Parser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#constantExpression.
    def exitConstantExpression(self, ctx:Java8Parser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#expression.
    def enterExpression(self, ctx:Java8Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#expression.
    def exitExpression(self, ctx:Java8Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#lambdaExpression.
    def enterLambdaExpression(self, ctx:Java8Parser.LambdaExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#lambdaExpression.
    def exitLambdaExpression(self, ctx:Java8Parser.LambdaExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#lambdaParameters.
    def enterLambdaParameters(self, ctx:Java8Parser.LambdaParametersContext):
        pass

    # Exit a parse tree produced by Java8Parser#lambdaParameters.
    def exitLambdaParameters(self, ctx:Java8Parser.LambdaParametersContext):
        pass


    # Enter a parse tree produced by Java8Parser#inferredFormalParameterList.
    def enterInferredFormalParameterList(self, ctx:Java8Parser.InferredFormalParameterListContext):
        pass

    # Exit a parse tree produced by Java8Parser#inferredFormalParameterList.
    def exitInferredFormalParameterList(self, ctx:Java8Parser.InferredFormalParameterListContext):
        pass


    # Enter a parse tree produced by Java8Parser#lambdaBody.
    def enterLambdaBody(self, ctx:Java8Parser.LambdaBodyContext):
        pass

    # Exit a parse tree produced by Java8Parser#lambdaBody.
    def exitLambdaBody(self, ctx:Java8Parser.LambdaBodyContext):
        pass


    # Enter a parse tree produced by Java8Parser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:Java8Parser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:Java8Parser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#assignment.
    def enterAssignment(self, ctx:Java8Parser.AssignmentContext):
        pass

    # Exit a parse tree produced by Java8Parser#assignment.
    def exitAssignment(self, ctx:Java8Parser.AssignmentContext):
        pass


    # Enter a parse tree produced by Java8Parser#leftHandSide.
    def enterLeftHandSide(self, ctx:Java8Parser.LeftHandSideContext):
        pass

    # Exit a parse tree produced by Java8Parser#leftHandSide.
    def exitLeftHandSide(self, ctx:Java8Parser.LeftHandSideContext):
        pass


    # Enter a parse tree produced by Java8Parser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:Java8Parser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by Java8Parser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:Java8Parser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by Java8Parser#conditionalExpression.
    def enterConditionalExpression(self, ctx:Java8Parser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#conditionalExpression.
    def exitConditionalExpression(self, ctx:Java8Parser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#conditionalOrExpression.
    def enterConditionalOrExpression(self, ctx:Java8Parser.ConditionalOrExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#conditionalOrExpression.
    def exitConditionalOrExpression(self, ctx:Java8Parser.ConditionalOrExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#conditionalAndExpression.
    def enterConditionalAndExpression(self, ctx:Java8Parser.ConditionalAndExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#conditionalAndExpression.
    def exitConditionalAndExpression(self, ctx:Java8Parser.ConditionalAndExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:Java8Parser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:Java8Parser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:Java8Parser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:Java8Parser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#andExpression.
    def enterAndExpression(self, ctx:Java8Parser.AndExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#andExpression.
    def exitAndExpression(self, ctx:Java8Parser.AndExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#equalityExpression.
    def enterEqualityExpression(self, ctx:Java8Parser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#equalityExpression.
    def exitEqualityExpression(self, ctx:Java8Parser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#relationalExpression.
    def enterRelationalExpression(self, ctx:Java8Parser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#relationalExpression.
    def exitRelationalExpression(self, ctx:Java8Parser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#shiftExpression.
    def enterShiftExpression(self, ctx:Java8Parser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#shiftExpression.
    def exitShiftExpression(self, ctx:Java8Parser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#additiveExpression.
    def enterAdditiveExpression(self, ctx:Java8Parser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#additiveExpression.
    def exitAdditiveExpression(self, ctx:Java8Parser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:Java8Parser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:Java8Parser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#unaryExpression.
    def enterUnaryExpression(self, ctx:Java8Parser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#unaryExpression.
    def exitUnaryExpression(self, ctx:Java8Parser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#preIncrementExpression.
    def enterPreIncrementExpression(self, ctx:Java8Parser.PreIncrementExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#preIncrementExpression.
    def exitPreIncrementExpression(self, ctx:Java8Parser.PreIncrementExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#preDecrementExpression.
    def enterPreDecrementExpression(self, ctx:Java8Parser.PreDecrementExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#preDecrementExpression.
    def exitPreDecrementExpression(self, ctx:Java8Parser.PreDecrementExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#unaryExpressionNotPlusMinus.
    def enterUnaryExpressionNotPlusMinus(self, ctx:Java8Parser.UnaryExpressionNotPlusMinusContext):
        pass

    # Exit a parse tree produced by Java8Parser#unaryExpressionNotPlusMinus.
    def exitUnaryExpressionNotPlusMinus(self, ctx:Java8Parser.UnaryExpressionNotPlusMinusContext):
        pass


    # Enter a parse tree produced by Java8Parser#postfixExpression.
    def enterPostfixExpression(self, ctx:Java8Parser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#postfixExpression.
    def exitPostfixExpression(self, ctx:Java8Parser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#postIncrementExpression.
    def enterPostIncrementExpression(self, ctx:Java8Parser.PostIncrementExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#postIncrementExpression.
    def exitPostIncrementExpression(self, ctx:Java8Parser.PostIncrementExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#postIncrementExpression_lf_postfixExpression.
    def enterPostIncrementExpression_lf_postfixExpression(self, ctx:Java8Parser.PostIncrementExpression_lf_postfixExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#postIncrementExpression_lf_postfixExpression.
    def exitPostIncrementExpression_lf_postfixExpression(self, ctx:Java8Parser.PostIncrementExpression_lf_postfixExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#postDecrementExpression.
    def enterPostDecrementExpression(self, ctx:Java8Parser.PostDecrementExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#postDecrementExpression.
    def exitPostDecrementExpression(self, ctx:Java8Parser.PostDecrementExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#postDecrementExpression_lf_postfixExpression.
    def enterPostDecrementExpression_lf_postfixExpression(self, ctx:Java8Parser.PostDecrementExpression_lf_postfixExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#postDecrementExpression_lf_postfixExpression.
    def exitPostDecrementExpression_lf_postfixExpression(self, ctx:Java8Parser.PostDecrementExpression_lf_postfixExpressionContext):
        pass


    # Enter a parse tree produced by Java8Parser#castExpression.
    def enterCastExpression(self, ctx:Java8Parser.CastExpressionContext):
        pass

    # Exit a parse tree produced by Java8Parser#castExpression.
    def exitCastExpression(self, ctx:Java8Parser.CastExpressionContext):
        pass



del Java8Parser