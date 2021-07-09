# Generated from Corundum.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CorundumParser import CorundumParser
else:
    from CorundumParser import CorundumParser

# This class defines a complete listener for a parse tree produced by CorundumParser.
class CorundumListener(ParseTreeListener):

    # Enter a parse tree produced by CorundumParser#prog.
    def enterProg(self, ctx:CorundumParser.ProgContext):
        pass

    # Exit a parse tree produced by CorundumParser#prog.
    def exitProg(self, ctx:CorundumParser.ProgContext):
        pass


    # Enter a parse tree produced by CorundumParser#expression_list.
    def enterExpression_list(self, ctx:CorundumParser.Expression_listContext):
        pass

    # Exit a parse tree produced by CorundumParser#expression_list.
    def exitExpression_list(self, ctx:CorundumParser.Expression_listContext):
        pass


    # Enter a parse tree produced by CorundumParser#expression.
    def enterExpression(self, ctx:CorundumParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CorundumParser#expression.
    def exitExpression(self, ctx:CorundumParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CorundumParser#global_get.
    def enterGlobal_get(self, ctx:CorundumParser.Global_getContext):
        pass

    # Exit a parse tree produced by CorundumParser#global_get.
    def exitGlobal_get(self, ctx:CorundumParser.Global_getContext):
        pass


    # Enter a parse tree produced by CorundumParser#global_set.
    def enterGlobal_set(self, ctx:CorundumParser.Global_setContext):
        pass

    # Exit a parse tree produced by CorundumParser#global_set.
    def exitGlobal_set(self, ctx:CorundumParser.Global_setContext):
        pass


    # Enter a parse tree produced by CorundumParser#global_result.
    def enterGlobal_result(self, ctx:CorundumParser.Global_resultContext):
        pass

    # Exit a parse tree produced by CorundumParser#global_result.
    def exitGlobal_result(self, ctx:CorundumParser.Global_resultContext):
        pass


    # Enter a parse tree produced by CorundumParser#function_inline_call.
    def enterFunction_inline_call(self, ctx:CorundumParser.Function_inline_callContext):
        pass

    # Exit a parse tree produced by CorundumParser#function_inline_call.
    def exitFunction_inline_call(self, ctx:CorundumParser.Function_inline_callContext):
        pass


    # Enter a parse tree produced by CorundumParser#require_block.
    def enterRequire_block(self, ctx:CorundumParser.Require_blockContext):
        pass

    # Exit a parse tree produced by CorundumParser#require_block.
    def exitRequire_block(self, ctx:CorundumParser.Require_blockContext):
        pass


    # Enter a parse tree produced by CorundumParser#pir_inline.
    def enterPir_inline(self, ctx:CorundumParser.Pir_inlineContext):
        pass

    # Exit a parse tree produced by CorundumParser#pir_inline.
    def exitPir_inline(self, ctx:CorundumParser.Pir_inlineContext):
        pass


    # Enter a parse tree produced by CorundumParser#pir_expression_list.
    def enterPir_expression_list(self, ctx:CorundumParser.Pir_expression_listContext):
        pass

    # Exit a parse tree produced by CorundumParser#pir_expression_list.
    def exitPir_expression_list(self, ctx:CorundumParser.Pir_expression_listContext):
        pass


    # Enter a parse tree produced by CorundumParser#function_definition.
    def enterFunction_definition(self, ctx:CorundumParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by CorundumParser#function_definition.
    def exitFunction_definition(self, ctx:CorundumParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by CorundumParser#function_definition_body.
    def enterFunction_definition_body(self, ctx:CorundumParser.Function_definition_bodyContext):
        pass

    # Exit a parse tree produced by CorundumParser#function_definition_body.
    def exitFunction_definition_body(self, ctx:CorundumParser.Function_definition_bodyContext):
        pass


    # Enter a parse tree produced by CorundumParser#function_definition_header.
    def enterFunction_definition_header(self, ctx:CorundumParser.Function_definition_headerContext):
        pass

    # Exit a parse tree produced by CorundumParser#function_definition_header.
    def exitFunction_definition_header(self, ctx:CorundumParser.Function_definition_headerContext):
        pass


    # Enter a parse tree produced by CorundumParser#function_name.
    def enterFunction_name(self, ctx:CorundumParser.Function_nameContext):
        pass

    # Exit a parse tree produced by CorundumParser#function_name.
    def exitFunction_name(self, ctx:CorundumParser.Function_nameContext):
        pass


    # Enter a parse tree produced by CorundumParser#function_definition_params.
    def enterFunction_definition_params(self, ctx:CorundumParser.Function_definition_paramsContext):
        pass

    # Exit a parse tree produced by CorundumParser#function_definition_params.
    def exitFunction_definition_params(self, ctx:CorundumParser.Function_definition_paramsContext):
        pass


    # Enter a parse tree produced by CorundumParser#function_definition_params_list.
    def enterFunction_definition_params_list(self, ctx:CorundumParser.Function_definition_params_listContext):
        pass

    # Exit a parse tree produced by CorundumParser#function_definition_params_list.
    def exitFunction_definition_params_list(self, ctx:CorundumParser.Function_definition_params_listContext):
        pass


    # Enter a parse tree produced by CorundumParser#function_definition_param_id.
    def enterFunction_definition_param_id(self, ctx:CorundumParser.Function_definition_param_idContext):
        pass

    # Exit a parse tree produced by CorundumParser#function_definition_param_id.
    def exitFunction_definition_param_id(self, ctx:CorundumParser.Function_definition_param_idContext):
        pass


    # Enter a parse tree produced by CorundumParser#return_statement.
    def enterReturn_statement(self, ctx:CorundumParser.Return_statementContext):
        pass

    # Exit a parse tree produced by CorundumParser#return_statement.
    def exitReturn_statement(self, ctx:CorundumParser.Return_statementContext):
        pass


    # Enter a parse tree produced by CorundumParser#function_call.
    def enterFunction_call(self, ctx:CorundumParser.Function_callContext):
        pass

    # Exit a parse tree produced by CorundumParser#function_call.
    def exitFunction_call(self, ctx:CorundumParser.Function_callContext):
        pass


    # Enter a parse tree produced by CorundumParser#function_call_param_list.
    def enterFunction_call_param_list(self, ctx:CorundumParser.Function_call_param_listContext):
        pass

    # Exit a parse tree produced by CorundumParser#function_call_param_list.
    def exitFunction_call_param_list(self, ctx:CorundumParser.Function_call_param_listContext):
        pass


    # Enter a parse tree produced by CorundumParser#function_call_params.
    def enterFunction_call_params(self, ctx:CorundumParser.Function_call_paramsContext):
        pass

    # Exit a parse tree produced by CorundumParser#function_call_params.
    def exitFunction_call_params(self, ctx:CorundumParser.Function_call_paramsContext):
        pass


    # Enter a parse tree produced by CorundumParser#function_param.
    def enterFunction_param(self, ctx:CorundumParser.Function_paramContext):
        pass

    # Exit a parse tree produced by CorundumParser#function_param.
    def exitFunction_param(self, ctx:CorundumParser.Function_paramContext):
        pass


    # Enter a parse tree produced by CorundumParser#function_unnamed_param.
    def enterFunction_unnamed_param(self, ctx:CorundumParser.Function_unnamed_paramContext):
        pass

    # Exit a parse tree produced by CorundumParser#function_unnamed_param.
    def exitFunction_unnamed_param(self, ctx:CorundumParser.Function_unnamed_paramContext):
        pass


    # Enter a parse tree produced by CorundumParser#function_named_param.
    def enterFunction_named_param(self, ctx:CorundumParser.Function_named_paramContext):
        pass

    # Exit a parse tree produced by CorundumParser#function_named_param.
    def exitFunction_named_param(self, ctx:CorundumParser.Function_named_paramContext):
        pass


    # Enter a parse tree produced by CorundumParser#function_call_assignment.
    def enterFunction_call_assignment(self, ctx:CorundumParser.Function_call_assignmentContext):
        pass

    # Exit a parse tree produced by CorundumParser#function_call_assignment.
    def exitFunction_call_assignment(self, ctx:CorundumParser.Function_call_assignmentContext):
        pass


    # Enter a parse tree produced by CorundumParser#all_result.
    def enterAll_result(self, ctx:CorundumParser.All_resultContext):
        pass

    # Exit a parse tree produced by CorundumParser#all_result.
    def exitAll_result(self, ctx:CorundumParser.All_resultContext):
        pass


    # Enter a parse tree produced by CorundumParser#elsif_statement.
    def enterElsif_statement(self, ctx:CorundumParser.Elsif_statementContext):
        pass

    # Exit a parse tree produced by CorundumParser#elsif_statement.
    def exitElsif_statement(self, ctx:CorundumParser.Elsif_statementContext):
        pass


    # Enter a parse tree produced by CorundumParser#if_elsif_statement.
    def enterIf_elsif_statement(self, ctx:CorundumParser.If_elsif_statementContext):
        pass

    # Exit a parse tree produced by CorundumParser#if_elsif_statement.
    def exitIf_elsif_statement(self, ctx:CorundumParser.If_elsif_statementContext):
        pass


    # Enter a parse tree produced by CorundumParser#if_statement.
    def enterIf_statement(self, ctx:CorundumParser.If_statementContext):
        pass

    # Exit a parse tree produced by CorundumParser#if_statement.
    def exitIf_statement(self, ctx:CorundumParser.If_statementContext):
        pass


    # Enter a parse tree produced by CorundumParser#unless_statement.
    def enterUnless_statement(self, ctx:CorundumParser.Unless_statementContext):
        pass

    # Exit a parse tree produced by CorundumParser#unless_statement.
    def exitUnless_statement(self, ctx:CorundumParser.Unless_statementContext):
        pass


    # Enter a parse tree produced by CorundumParser#while_statement.
    def enterWhile_statement(self, ctx:CorundumParser.While_statementContext):
        pass

    # Exit a parse tree produced by CorundumParser#while_statement.
    def exitWhile_statement(self, ctx:CorundumParser.While_statementContext):
        pass


    # Enter a parse tree produced by CorundumParser#for_statement.
    def enterFor_statement(self, ctx:CorundumParser.For_statementContext):
        pass

    # Exit a parse tree produced by CorundumParser#for_statement.
    def exitFor_statement(self, ctx:CorundumParser.For_statementContext):
        pass


    # Enter a parse tree produced by CorundumParser#init_expression.
    def enterInit_expression(self, ctx:CorundumParser.Init_expressionContext):
        pass

    # Exit a parse tree produced by CorundumParser#init_expression.
    def exitInit_expression(self, ctx:CorundumParser.Init_expressionContext):
        pass


    # Enter a parse tree produced by CorundumParser#all_assignment.
    def enterAll_assignment(self, ctx:CorundumParser.All_assignmentContext):
        pass

    # Exit a parse tree produced by CorundumParser#all_assignment.
    def exitAll_assignment(self, ctx:CorundumParser.All_assignmentContext):
        pass


    # Enter a parse tree produced by CorundumParser#for_init_list.
    def enterFor_init_list(self, ctx:CorundumParser.For_init_listContext):
        pass

    # Exit a parse tree produced by CorundumParser#for_init_list.
    def exitFor_init_list(self, ctx:CorundumParser.For_init_listContext):
        pass


    # Enter a parse tree produced by CorundumParser#cond_expression.
    def enterCond_expression(self, ctx:CorundumParser.Cond_expressionContext):
        pass

    # Exit a parse tree produced by CorundumParser#cond_expression.
    def exitCond_expression(self, ctx:CorundumParser.Cond_expressionContext):
        pass


    # Enter a parse tree produced by CorundumParser#loop_expression.
    def enterLoop_expression(self, ctx:CorundumParser.Loop_expressionContext):
        pass

    # Exit a parse tree produced by CorundumParser#loop_expression.
    def exitLoop_expression(self, ctx:CorundumParser.Loop_expressionContext):
        pass


    # Enter a parse tree produced by CorundumParser#for_loop_list.
    def enterFor_loop_list(self, ctx:CorundumParser.For_loop_listContext):
        pass

    # Exit a parse tree produced by CorundumParser#for_loop_list.
    def exitFor_loop_list(self, ctx:CorundumParser.For_loop_listContext):
        pass


    # Enter a parse tree produced by CorundumParser#statement_body.
    def enterStatement_body(self, ctx:CorundumParser.Statement_bodyContext):
        pass

    # Exit a parse tree produced by CorundumParser#statement_body.
    def exitStatement_body(self, ctx:CorundumParser.Statement_bodyContext):
        pass


    # Enter a parse tree produced by CorundumParser#statement_expression_list.
    def enterStatement_expression_list(self, ctx:CorundumParser.Statement_expression_listContext):
        pass

    # Exit a parse tree produced by CorundumParser#statement_expression_list.
    def exitStatement_expression_list(self, ctx:CorundumParser.Statement_expression_listContext):
        pass


    # Enter a parse tree produced by CorundumParser#assignment.
    def enterAssignment(self, ctx:CorundumParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CorundumParser#assignment.
    def exitAssignment(self, ctx:CorundumParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CorundumParser#dynamic_assignment.
    def enterDynamic_assignment(self, ctx:CorundumParser.Dynamic_assignmentContext):
        pass

    # Exit a parse tree produced by CorundumParser#dynamic_assignment.
    def exitDynamic_assignment(self, ctx:CorundumParser.Dynamic_assignmentContext):
        pass


    # Enter a parse tree produced by CorundumParser#int_assignment.
    def enterInt_assignment(self, ctx:CorundumParser.Int_assignmentContext):
        pass

    # Exit a parse tree produced by CorundumParser#int_assignment.
    def exitInt_assignment(self, ctx:CorundumParser.Int_assignmentContext):
        pass


    # Enter a parse tree produced by CorundumParser#float_assignment.
    def enterFloat_assignment(self, ctx:CorundumParser.Float_assignmentContext):
        pass

    # Exit a parse tree produced by CorundumParser#float_assignment.
    def exitFloat_assignment(self, ctx:CorundumParser.Float_assignmentContext):
        pass


    # Enter a parse tree produced by CorundumParser#string_assignment.
    def enterString_assignment(self, ctx:CorundumParser.String_assignmentContext):
        pass

    # Exit a parse tree produced by CorundumParser#string_assignment.
    def exitString_assignment(self, ctx:CorundumParser.String_assignmentContext):
        pass


    # Enter a parse tree produced by CorundumParser#initial_array_assignment.
    def enterInitial_array_assignment(self, ctx:CorundumParser.Initial_array_assignmentContext):
        pass

    # Exit a parse tree produced by CorundumParser#initial_array_assignment.
    def exitInitial_array_assignment(self, ctx:CorundumParser.Initial_array_assignmentContext):
        pass


    # Enter a parse tree produced by CorundumParser#array_assignment.
    def enterArray_assignment(self, ctx:CorundumParser.Array_assignmentContext):
        pass

    # Exit a parse tree produced by CorundumParser#array_assignment.
    def exitArray_assignment(self, ctx:CorundumParser.Array_assignmentContext):
        pass


    # Enter a parse tree produced by CorundumParser#array_definition.
    def enterArray_definition(self, ctx:CorundumParser.Array_definitionContext):
        pass

    # Exit a parse tree produced by CorundumParser#array_definition.
    def exitArray_definition(self, ctx:CorundumParser.Array_definitionContext):
        pass


    # Enter a parse tree produced by CorundumParser#array_definition_elements.
    def enterArray_definition_elements(self, ctx:CorundumParser.Array_definition_elementsContext):
        pass

    # Exit a parse tree produced by CorundumParser#array_definition_elements.
    def exitArray_definition_elements(self, ctx:CorundumParser.Array_definition_elementsContext):
        pass


    # Enter a parse tree produced by CorundumParser#array_selector.
    def enterArray_selector(self, ctx:CorundumParser.Array_selectorContext):
        pass

    # Exit a parse tree produced by CorundumParser#array_selector.
    def exitArray_selector(self, ctx:CorundumParser.Array_selectorContext):
        pass


    # Enter a parse tree produced by CorundumParser#dynamic_result.
    def enterDynamic_result(self, ctx:CorundumParser.Dynamic_resultContext):
        pass

    # Exit a parse tree produced by CorundumParser#dynamic_result.
    def exitDynamic_result(self, ctx:CorundumParser.Dynamic_resultContext):
        pass


    # Enter a parse tree produced by CorundumParser#dynamic_.
    def enterDynamic_(self, ctx:CorundumParser.Dynamic_Context):
        pass

    # Exit a parse tree produced by CorundumParser#dynamic_.
    def exitDynamic_(self, ctx:CorundumParser.Dynamic_Context):
        pass


    # Enter a parse tree produced by CorundumParser#int_result.
    def enterInt_result(self, ctx:CorundumParser.Int_resultContext):
        pass

    # Exit a parse tree produced by CorundumParser#int_result.
    def exitInt_result(self, ctx:CorundumParser.Int_resultContext):
        pass


    # Enter a parse tree produced by CorundumParser#float_result.
    def enterFloat_result(self, ctx:CorundumParser.Float_resultContext):
        pass

    # Exit a parse tree produced by CorundumParser#float_result.
    def exitFloat_result(self, ctx:CorundumParser.Float_resultContext):
        pass


    # Enter a parse tree produced by CorundumParser#string_result.
    def enterString_result(self, ctx:CorundumParser.String_resultContext):
        pass

    # Exit a parse tree produced by CorundumParser#string_result.
    def exitString_result(self, ctx:CorundumParser.String_resultContext):
        pass


    # Enter a parse tree produced by CorundumParser#comparison_list.
    def enterComparison_list(self, ctx:CorundumParser.Comparison_listContext):
        pass

    # Exit a parse tree produced by CorundumParser#comparison_list.
    def exitComparison_list(self, ctx:CorundumParser.Comparison_listContext):
        pass


    # Enter a parse tree produced by CorundumParser#comparison.
    def enterComparison(self, ctx:CorundumParser.ComparisonContext):
        pass

    # Exit a parse tree produced by CorundumParser#comparison.
    def exitComparison(self, ctx:CorundumParser.ComparisonContext):
        pass


    # Enter a parse tree produced by CorundumParser#comp_var.
    def enterComp_var(self, ctx:CorundumParser.Comp_varContext):
        pass

    # Exit a parse tree produced by CorundumParser#comp_var.
    def exitComp_var(self, ctx:CorundumParser.Comp_varContext):
        pass


    # Enter a parse tree produced by CorundumParser#lvalue.
    def enterLvalue(self, ctx:CorundumParser.LvalueContext):
        pass

    # Exit a parse tree produced by CorundumParser#lvalue.
    def exitLvalue(self, ctx:CorundumParser.LvalueContext):
        pass


    # Enter a parse tree produced by CorundumParser#rvalue.
    def enterRvalue(self, ctx:CorundumParser.RvalueContext):
        pass

    # Exit a parse tree produced by CorundumParser#rvalue.
    def exitRvalue(self, ctx:CorundumParser.RvalueContext):
        pass


    # Enter a parse tree produced by CorundumParser#break_expression.
    def enterBreak_expression(self, ctx:CorundumParser.Break_expressionContext):
        pass

    # Exit a parse tree produced by CorundumParser#break_expression.
    def exitBreak_expression(self, ctx:CorundumParser.Break_expressionContext):
        pass


    # Enter a parse tree produced by CorundumParser#literal_t.
    def enterLiteral_t(self, ctx:CorundumParser.Literal_tContext):
        pass

    # Exit a parse tree produced by CorundumParser#literal_t.
    def exitLiteral_t(self, ctx:CorundumParser.Literal_tContext):
        pass


    # Enter a parse tree produced by CorundumParser#float_t.
    def enterFloat_t(self, ctx:CorundumParser.Float_tContext):
        pass

    # Exit a parse tree produced by CorundumParser#float_t.
    def exitFloat_t(self, ctx:CorundumParser.Float_tContext):
        pass


    # Enter a parse tree produced by CorundumParser#int_t.
    def enterInt_t(self, ctx:CorundumParser.Int_tContext):
        pass

    # Exit a parse tree produced by CorundumParser#int_t.
    def exitInt_t(self, ctx:CorundumParser.Int_tContext):
        pass


    # Enter a parse tree produced by CorundumParser#bool_t.
    def enterBool_t(self, ctx:CorundumParser.Bool_tContext):
        pass

    # Exit a parse tree produced by CorundumParser#bool_t.
    def exitBool_t(self, ctx:CorundumParser.Bool_tContext):
        pass


    # Enter a parse tree produced by CorundumParser#nil_t.
    def enterNil_t(self, ctx:CorundumParser.Nil_tContext):
        pass

    # Exit a parse tree produced by CorundumParser#nil_t.
    def exitNil_t(self, ctx:CorundumParser.Nil_tContext):
        pass


    # Enter a parse tree produced by CorundumParser#id_.
    def enterId_(self, ctx:CorundumParser.Id_Context):
        pass

    # Exit a parse tree produced by CorundumParser#id_.
    def exitId_(self, ctx:CorundumParser.Id_Context):
        pass


    # Enter a parse tree produced by CorundumParser#id_global.
    def enterId_global(self, ctx:CorundumParser.Id_globalContext):
        pass

    # Exit a parse tree produced by CorundumParser#id_global.
    def exitId_global(self, ctx:CorundumParser.Id_globalContext):
        pass


    # Enter a parse tree produced by CorundumParser#id_function.
    def enterId_function(self, ctx:CorundumParser.Id_functionContext):
        pass

    # Exit a parse tree produced by CorundumParser#id_function.
    def exitId_function(self, ctx:CorundumParser.Id_functionContext):
        pass


    # Enter a parse tree produced by CorundumParser#terminator.
    def enterTerminator(self, ctx:CorundumParser.TerminatorContext):
        pass

    # Exit a parse tree produced by CorundumParser#terminator.
    def exitTerminator(self, ctx:CorundumParser.TerminatorContext):
        pass


    # Enter a parse tree produced by CorundumParser#else_token.
    def enterElse_token(self, ctx:CorundumParser.Else_tokenContext):
        pass

    # Exit a parse tree produced by CorundumParser#else_token.
    def exitElse_token(self, ctx:CorundumParser.Else_tokenContext):
        pass


    # Enter a parse tree produced by CorundumParser#crlf.
    def enterCrlf(self, ctx:CorundumParser.CrlfContext):
        pass

    # Exit a parse tree produced by CorundumParser#crlf.
    def exitCrlf(self, ctx:CorundumParser.CrlfContext):
        pass



del CorundumParser