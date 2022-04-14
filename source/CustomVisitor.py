# Generated from .\source\PAM.g4 by ANTLR 4.9.2
from antlr4 import *
from gen.PAMParser import PAMParser
from gen.PAMVisitor import PAMVisitor
from antlr4.tree.Tree import TerminalNode
import operator


# Visitor for PAM language.
class CustomVisitor(PAMVisitor):
    variables = {}  # Storing the variable values
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '<>': operator.ne,
        '=<': operator.le,
        '>=': operator.ge,
        '=': operator.eq,
        '<': operator.lt,
        '>': operator.gt,
        'NOT': operator.not_,
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
        # input_stmt: 'read' varlist;
        varlist = self.visitChildren(ctx)  # visitVarlist

        data_values = open('source/data.txt', 'r').read().split(',')
        # Assumption: only positive integers are passed
        for idx, var in enumerate(varlist):
            self.variables[var] = int(data_values[idx])

    # Visit a parse tree produced by PAMParser#output_stmt.
    def visitOutput_stmt(self, ctx: PAMParser.Output_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PAMParser#assign_stmt.
    def visitAssign_stmt(self, ctx: PAMParser.Assign_stmtContext):
        # assign_stmt : VARNAME ':=' (logical_expr|expr);
        self.variables[str(ctx.getChild(0))] = self.visit(ctx.getChild(2))
        print(self.variables)

    # Visit a parse tree produced by PAMParser#cond_stmt.
    def visitCond_stmt(self, ctx: PAMParser.Cond_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PAMParser#loop.
    def visitLoop(self, ctx: PAMParser.LoopContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PAMParser#compar.
    def visitCompar(self, ctx: PAMParser.ComparContext):
        # compar : expr RELATION expr;
        elem1 = self.visit(ctx.getChild(0))
        elem2 = self.visit(ctx.getChild(2))

        return self.ops[str(ctx.getChild(1))](elem1, elem2)

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
        # expr : term (WEAKOP term)*;
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)

        elem1 = self.visit(ctx.getChild(0))
        elem2 = self.visit(ctx.getChild(2))

        return round(self.ops[str(ctx.getChild(1))](elem1, elem2))

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
        # elem : NUMBER | VARNAME | '(' expr ')';
        if ctx.getChildCount() != 1:
            # if contains parenthesis
            return self.visit(ctx.getChild(1))  # visitExpr

        elem = str(ctx.getChild(0))

        if elem.isnumeric():
            return int(elem)

        return self.variables.get(elem)

    # Visit a parse tree produced by PAMParser#logical_expr.
    def visitLogical_expr(self, ctx: PAMParser.Logical_exprContext):
        # logical_expr :  logical_term (WEAKBOOL logical_term)*;
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)

        elem1 = self.visit(ctx.getChild(0))
        elem2 = self.visit(ctx.getChild(2))

        return elem1 or elem2

    # Visit a parse tree produced by PAMParser#logical_term.
    def visitLogical_term(self, ctx: PAMParser.Logical_termContext):
        # logical_term : logical_elem (STRONGBOOL logical_elem)*;
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)

        elem1 = self.visit(ctx.getChild(0))
        elem2 = self.visit(ctx.getChild(2))

        return elem1 and elem2

    # Visit a parse tree produced by PAMParser#logical_elem.
    def visitLogical_elem(self, ctx: PAMParser.Logical_elemContext):
        # logical_elem : (NEG)*? (compar|BOOL|VARNAME|'(' logical_expr ')');
        if ctx.getChildCount() > 1:
            if str(ctx.getChild(0)) == 'NOT':
                if ctx.getChildCount() == 2:
                    # NOT without parenthesis
                    if isinstance(ctx.getChild(1), TerminalNode):
                        # NOT terminal
                        elem = str(ctx.getChild(1))

                        # Converting strings to True and False
                        if eval(elem) in (True, False):
                            return self.ops[str(ctx.getChild(0))](eval(elem))
                    else:
                        return self.ops[str(ctx.getChild(0))](self.visit(ctx.getChild(1)))  # visitLogicalExpr
                else:
                    # NOT with parenthesis
                    # Exmp: NOT (True)
                    return self.ops[str(ctx.getChild(0))](self.visit(ctx.getChild(2)))  # visitLogicalExpr
            elif str(ctx.getChild(0)) == '(':
                # NOT (smth)
                return self.visit(ctx.getChild(2))
            else:
                # compar
                return self.visitChildren(ctx)

        if not isinstance(ctx.getChild(0), TerminalNode):
            # comprar handling
            elem = str(self.visitChildren(ctx))
        else:
            # Processing the single value that is BOOL, VARNAME
            elem = str(ctx.getChild(0))

        # Converting strings to True and False
        if eval(elem) in (True, False):
            return eval(elem)

        # Getting the value of variable
        return self.variables.get(elem)


del PAMParser
