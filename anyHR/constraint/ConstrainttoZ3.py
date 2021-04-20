from z3 import *
from parser.LRAParserVisitor import LRAParserVisitor

class LRAtoZ3(LRAParserVisitor):
    '''
    This class translates the LRA to its Z3 representation
    '''

    def __init__(self, ctx):
        self.ctx = ctx

    def translate(self):
        """Returns the Z3 translation of the NLRA constraint"""
        return self.visit(self.ctx)

    def visitLRA_Eq(self, ctx):
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return exp_1 == exp_2

    def visitLRA_Neq(self, ctx):
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return exp_1 != exp_2

    def visitLRA_GEQ(self, ctx):
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return exp_1 >= exp_2

    def visitLRA_LEQ(self, ctx):
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return exp_1 <= exp_2

    def visitLRA_Greater(self, ctx):
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return exp_1 > exp_2

    def visitLRA_Less(self, ctx):
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return exp_1 < exp_2

    def visitLRA_In(self, ctx):
        exp = self.visit(ctx.expression(0))
        exp_low = self.visit(ctx.expression(1))
        exp_up = self.visit(ctx.expression(2))
        return And(exp_low < exp, exp < exp_up)

    def visitExpressionExponential(self, ctx):
        exp = self.visit(ctx.expression())
        return exp

    def visitExpressionAddition(self, ctx):
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return exp_1 + exp_2

    def visitExpressionSubtraction(self, ctx):
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return exp_1 - exp_2

    def visitExpressionMultiplication(self, ctx):
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return exp_1 * exp_2

    def visitExpressionVariable(self, ctx):
        var_name = ctx.Identifier().getText()
        var = Real(var_name)
        return var

    def visitExpressionConstant(self, ctx):
        constant = RealVal(float(ctx.literal().getText()))
        return constant

    def visitExpressionParanthesis(self, ctx):
        return self.visit(ctx.expression())