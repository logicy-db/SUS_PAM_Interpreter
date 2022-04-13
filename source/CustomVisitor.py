# Generated from .\source\PAM.g4 by ANTLR 4.9.2
from antlr4 import *
from gen.PAMParser import PAMParser
from gen.PAMVisitor import PAMVisitor
import operator

# Visitor for PAM language.
class CustomVisitor(PAMVisitor):
    variables = {}  # Storing the variable values
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    # Visit a parse tree produced by PAMParser#progr.
    def visitProgr(self, ctx: PAMParser.ProgrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PAMParser#series.
    def visitSeries(self, ctx: PAMParser.SeriesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PAMParser#stmt.
    def visitStmt(self, ctx: PAMParser.StmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PAMParser#input_stmt.
    def visitInput_stmt(self, ctx: PAMParser.Input_stmtContext):
        #input_stmt: 'read' varlist;
        varlist = self.visitChildren(ctx) #visitVarlist

        data_values = open('source/data.txt', 'r').read().split(',')
        # Assumption: only positive integers are passed
        for idx, var in enumerate(varlist):
            self.variables[var] = int(data_values[idx])
        # print(self.variables)

    # Visit a parse tree produced by PAMParser#output_stmt.
    def visitOutput_stmt(self, ctx: PAMParser.Output_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PAMParser#assign_stmt.
    def visitAssign_stmt(self, ctx: PAMParser.Assign_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PAMParser#cond_stmt.
    def visitCond_stmt(self, ctx: PAMParser.Cond_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PAMParser#loop.
    def visitLoop(self, ctx: PAMParser.LoopContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PAMParser#compar.
    def visitCompar(self, ctx: PAMParser.ComparContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PAMParser#varlist.
    def visitVarlist(self, ctx: PAMParser.VarlistContext):
        # varlist : VARNAME (',' VARNAME)*;
        varlist = []

        for variable in [str(i) for i in ctx.getChildren()]:
            if variable != ',':
                varlist += variable

        return varlist

    # Visit a parse tree produced by PAMParser#expr.
    def visitExpr(self, ctx: PAMParser.ExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PAMParser#term.
    def visitTerm(self, ctx: PAMParser.TermContext):
        # term : elem (STRONGOP elem)*;
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)

        elem1 = self.visit(ctx.getChild(0))
        elem2 = self.visit(ctx.getChild(2))

        return round(self.ops[str(ctx.getChild(1))](elem1, elem2))

    # Visit a parse tree produced by PAMParser#elem.
    def visitElem(self, ctx: PAMParser.ElemContext):
        # elem : NUMBER | VARNAME | '('expr ')';
        if ctx.getChildCount() != 1:
            return self.visitChildren(ctx)  #visitExpr

        elem = str(ctx.getChild(0))

        return int(self.variables.get(elem))

    # Visit a parse tree produced by PAMParser#logical_expr.
    def visitLogical_expr(self, ctx: PAMParser.Logical_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PAMParser#logical_term.
    def visitLogical_term(self, ctx: PAMParser.Logical_termContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PAMParser#logical_elem.
    def visitLogical_elem(self, ctx: PAMParser.Logical_elemContext):
        return self.visitChildren(ctx)


del PAMParser
