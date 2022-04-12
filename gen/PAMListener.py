# Generated from .\source\PAM.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PAMParser import PAMParser
else:
    from PAMParser import PAMParser

# This class defines a complete listener for a parse tree produced by PAMParser.
class PAMListener(ParseTreeListener):

    # Enter a parse tree produced by PAMParser#progr.
    def enterProgr(self, ctx:PAMParser.ProgrContext):
        pass

    # Exit a parse tree produced by PAMParser#progr.
    def exitProgr(self, ctx:PAMParser.ProgrContext):
        pass


    # Enter a parse tree produced by PAMParser#series.
    def enterSeries(self, ctx:PAMParser.SeriesContext):
        pass

    # Exit a parse tree produced by PAMParser#series.
    def exitSeries(self, ctx:PAMParser.SeriesContext):
        pass


    # Enter a parse tree produced by PAMParser#stmt.
    def enterStmt(self, ctx:PAMParser.StmtContext):
        pass

    # Exit a parse tree produced by PAMParser#stmt.
    def exitStmt(self, ctx:PAMParser.StmtContext):
        pass


    # Enter a parse tree produced by PAMParser#input_stmt.
    def enterInput_stmt(self, ctx:PAMParser.Input_stmtContext):
        pass

    # Exit a parse tree produced by PAMParser#input_stmt.
    def exitInput_stmt(self, ctx:PAMParser.Input_stmtContext):
        pass


    # Enter a parse tree produced by PAMParser#output_stmt.
    def enterOutput_stmt(self, ctx:PAMParser.Output_stmtContext):
        pass

    # Exit a parse tree produced by PAMParser#output_stmt.
    def exitOutput_stmt(self, ctx:PAMParser.Output_stmtContext):
        pass


    # Enter a parse tree produced by PAMParser#assign_stmt.
    def enterAssign_stmt(self, ctx:PAMParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by PAMParser#assign_stmt.
    def exitAssign_stmt(self, ctx:PAMParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by PAMParser#cond_stmt.
    def enterCond_stmt(self, ctx:PAMParser.Cond_stmtContext):
        pass

    # Exit a parse tree produced by PAMParser#cond_stmt.
    def exitCond_stmt(self, ctx:PAMParser.Cond_stmtContext):
        pass


    # Enter a parse tree produced by PAMParser#loop.
    def enterLoop(self, ctx:PAMParser.LoopContext):
        pass

    # Exit a parse tree produced by PAMParser#loop.
    def exitLoop(self, ctx:PAMParser.LoopContext):
        pass


    # Enter a parse tree produced by PAMParser#compar.
    def enterCompar(self, ctx:PAMParser.ComparContext):
        pass

    # Exit a parse tree produced by PAMParser#compar.
    def exitCompar(self, ctx:PAMParser.ComparContext):
        pass


    # Enter a parse tree produced by PAMParser#varlist.
    def enterVarlist(self, ctx:PAMParser.VarlistContext):
        pass

    # Exit a parse tree produced by PAMParser#varlist.
    def exitVarlist(self, ctx:PAMParser.VarlistContext):
        pass


    # Enter a parse tree produced by PAMParser#expr.
    def enterExpr(self, ctx:PAMParser.ExprContext):
        pass

    # Exit a parse tree produced by PAMParser#expr.
    def exitExpr(self, ctx:PAMParser.ExprContext):
        pass


    # Enter a parse tree produced by PAMParser#term.
    def enterTerm(self, ctx:PAMParser.TermContext):
        pass

    # Exit a parse tree produced by PAMParser#term.
    def exitTerm(self, ctx:PAMParser.TermContext):
        pass


    # Enter a parse tree produced by PAMParser#elem.
    def enterElem(self, ctx:PAMParser.ElemContext):
        pass

    # Exit a parse tree produced by PAMParser#elem.
    def exitElem(self, ctx:PAMParser.ElemContext):
        pass


    # Enter a parse tree produced by PAMParser#logical_expr.
    def enterLogical_expr(self, ctx:PAMParser.Logical_exprContext):
        pass

    # Exit a parse tree produced by PAMParser#logical_expr.
    def exitLogical_expr(self, ctx:PAMParser.Logical_exprContext):
        pass


    # Enter a parse tree produced by PAMParser#logical_term.
    def enterLogical_term(self, ctx:PAMParser.Logical_termContext):
        pass

    # Exit a parse tree produced by PAMParser#logical_term.
    def exitLogical_term(self, ctx:PAMParser.Logical_termContext):
        pass


    # Enter a parse tree produced by PAMParser#logical_elem.
    def enterLogical_elem(self, ctx:PAMParser.Logical_elemContext):
        pass

    # Exit a parse tree produced by PAMParser#logical_elem.
    def exitLogical_elem(self, ctx:PAMParser.Logical_elemContext):
        pass



del PAMParser