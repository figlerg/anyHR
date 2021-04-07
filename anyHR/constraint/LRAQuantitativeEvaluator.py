from z3 import *
from prs.LRAParserVisitor import LRAParserVisitor

class LRAQuantitativeEvaluator(LRAParserVisitor):
    """
    This class evaluates to True or False a LRA expression by substituting variables
    with concrete numbers, given as input
    """

    def __init__(self, ctx, var_name_list: list):
        self.ctx = ctx
        self.var_name_idx_dict = dict()
        self.sample = []

        # Create a dictionary mapping var names to array indices
        i = 0
        for var_name in var_name_list:
            self.var_name_idx_dict[var_name] = i
            i += 1

    def evaluate(self, sample: list) -> float:
        self.sample = sample
        out = self.visit(self.ctx)
        return out

    def visitLRA_Eq(self, ctx) -> float:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return - abs(exp_1 - exp_2)

    def visitLRA_Neq(self, ctx) -> float:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return abs(exp_1 - exp_2)

    def visitLRA_GEQ(self, ctx) -> float:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return exp_1 - exp_2

    def visitLRA_LEQ(self, ctx) -> float:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return exp_2 - exp_1

    def visitLRA_Greater(self, ctx) -> float:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return exp_1 - exp_2

    def visitLRA_Less(self, ctx) -> float:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return exp_2 - exp_1

    def visitExpressionAddition(self, ctx) -> float:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return exp_1 + exp_2

    def visitLRA_In(self, ctx):
        exp = self.visit(ctx.expression(0))
        exp_low = self.visit(ctx.expression(1))
        exp_up = self.visit(ctx.expression(2))
        return min(exp - exp_low, exp_up - exp)

    def visitExpressionSubtraction(self, ctx) -> float:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return exp_1 - exp_2

    def visitExpressionMultiplication(self, ctx) -> float:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return exp_1 * exp_2

    def visitExpressionExponential(self, ctx) -> float:
        exp = self.visit(ctx.expression())
        return math.exp(exp)

    def visitExpressionVariable(self, ctx) -> float:
        var_name = ctx.Identifier().getText()
        idx = self.var_name_idx_dict[var_name]
        var = self.sample[idx]
        return var

    def visitExpressionConstant(self, ctx) -> float:
        constant = float(ctx.literal().getText())
        return constant

    def visitExpressionParanthesis(self, ctx):
        return self.visit(ctx.expression())