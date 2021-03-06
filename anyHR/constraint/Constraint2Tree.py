from anyHR.constraint.parser.ConstraintParserVisitor import ConstraintParserVisitor
from anyHR.constraint.node.Node import *


class Constraint2Tree(ConstraintParserVisitor):
    """
    Use the ANTLR Parser to create our own tree (Node structure in Node.py).
    Return a tree as node with translate()
    """

    def __init__(self, ctx):
        self.ctx = ctx


    # api
    def translate(self):
        return self.visit(self.ctx)

    def visitLRA_LEQ(self, ctx) -> Node:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return LEQ(exp_1, exp_2)

    def visitLRA_GEQ(self, ctx) -> Node:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return GEQ(exp_1, exp_2)

    def visitLRA_Less(self, ctx) -> Node:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return Less(exp_1, exp_2)

    def visitLRA_Greater(self, ctx) -> Node:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return Greater(exp_1, exp_2)

    def visitLRA_Eq(self, ctx) -> Node:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return EQ(exp_1, exp_2)

    def visitLRA_Neq(self, ctx) -> Node:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return NEQ(exp_1, exp_2)

    def visitLRA_In(self, ctx):
        exp = self.visit(ctx.expression(0))
        exp_low = self.visit(ctx.expression(1))
        exp_up = self.visit(ctx.expression(2))
        return In(exp, exp_low, exp_up)

    def visitExpressionVariable(self, ctx) -> Node:
        var_name = ctx.Identifier().getText()
        var = Variable(var_name)
        return var

    def visitExpressionConstant(self, ctx) -> Node:
        value = float(ctx.literal().getText())
        constant = Constant(value)
        return constant

    def visitExpressionAddition(self, ctx) -> Node:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))

        exp = Addition(exp_1, exp_2)

        return exp

    def visitExpressionSubtraction(self, ctx) -> Node:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return Subtraction(exp_1, exp_2)

    def visitExpressionMultiplication(self, ctx) -> Node:
        exp_1 = self.visit(ctx.expression(0))
        exp_2 = self.visit(ctx.expression(1))
        return Multiplication(exp_1, exp_2)

    def visitExpressionExponential(self, ctx) -> Node:
        exp = self.visit(ctx.expression())
        return Exponential(exp)

    def visitExpressionParanthesis(self, ctx):
        return self.visit(ctx.expression())
