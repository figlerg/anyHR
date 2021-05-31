from z3 import *

from anyHR.constraint.node.Node import *
from anyHR.constraint.node.Visitor import NodeVisitor


class ConstrainttoZ3(NodeVisitor):
    '''
    This class translates the constraint tree to its Z3 representation
    '''

    def __init__(self, node: Node):
        self.node = node

    # api
    def translate(self) -> ExprRef:
        """Returns the Z3 translation of the NLRA constraint"""
        return self.visit(self.node, None)

    def visitLEQ(self, node: LEQ, args):
        exp_1: ExprRef = self.visit(node.children[0], args)
        exp_2: ExprRef = self.visit(node.children[1], args)
        return exp_1 <= exp_2

    def visitGEQ(self, node: GEQ, args):
        exp_1: ExprRef = self.visit(node.children[0], args)
        exp_2: ExprRef = self.visit(node.children[1], args)
        return exp_1 >= exp_2

    def visitGreater(self, node: Greater, args):
        exp_1: ExprRef = self.visit(node.children[0], args)
        exp_2: ExprRef = self.visit(node.children[1], args)
        return exp_1 > exp_2

    def visitLess(self, node: Less, args):
        exp_1: ExprRef = self.visit(node.children[0], args)
        exp_2: ExprRef = self.visit(node.children[1], args)
        return exp_1 < exp_2

    def visitEQ(self, node: EQ, args) -> ExprRef:
        exp_1: ExprRef = self.visit(node.children[0], args)
        exp_2: ExprRef = self.visit(node.children[1], args)
        return exp_1 == exp_2

    def visitNEQ(self, node: NEQ, args):
        exp_1: ExprRef = self.visit(node.children[0], args)
        exp_2: ExprRef = self.visit(node.children[1], args)
        return exp_1 != exp_2

    def visitIn(self, node: In, args) -> ExprRef:
        exp: ExprRef = self.visit(node.children[0], args)
        exp_low: ExprRef = self.visit(node.children[1], args)
        exp_up: ExprRef = self.visit(node.children[2], args)
        return And(exp_low < exp, exp < exp_up)

    def visitVariable(self, node: Variable, args) -> ExprRef:
        var_name = node.name

        var = Real(var_name)
        return var

    def visitConstant(self, node: Constant, args) -> ExprRef:
        constant = RealVal(node.value)
        return constant

    def visitAddition(self, node: Addition, args) -> ExprRef:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 + exp_2

    def visitSubtraction(self, node: Subtraction, args) -> ExprRef:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 - exp_2

    def visitMultiplication(self, node: Multiplication, args) -> ExprRef:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 * exp_2

    def visitExponential(self, node: Exponential, args):
        exp = self.visit(node.children[0], args)
        raise Exception('Exponentials cannot be translated to Z3')

    # def __init__(self, ctx):
    #     self.ctx = ctx
    #
    # def translate(self):
    #     """Returns the Z3 translation of the NLRA constraint"""
    #     return self.visit(self.ctx)
    #
    # def visitLRA_Eq(self, ctx):
    #     exp_1 = self.visit(ctx.expression(0))
    #     exp_2 = self.visit(ctx.expression(1))
    #     return exp_1 == exp_2
    #
    # def visitLRA_Neq(self, ctx):
    #     exp_1 = self.visit(ctx.expression(0))
    #     exp_2 = self.visit(ctx.expression(1))
    #     return exp_1 != exp_2
    #
    # def visitLRA_GEQ(self, ctx):
    #     exp_1 = self.visit(ctx.expression(0))
    #     exp_2 = self.visit(ctx.expression(1))
    #     return exp_1 >= exp_2
    #
    # def visitLRA_LEQ(self, ctx):
    #     exp_1 = self.visit(ctx.expression(0))
    #     exp_2 = self.visit(ctx.expression(1))
    #     return exp_1 <= exp_2
    #
    # def visitLRA_Greater(self, ctx):
    #     exp_1 = self.visit(ctx.expression(0))
    #     exp_2 = self.visit(ctx.expression(1))
    #     return exp_1 > exp_2
    #
    # def visitLRA_Less(self, ctx):
    #     exp_1 = self.visit(ctx.expression(0))
    #     exp_2 = self.visit(ctx.expression(1))
    #     return exp_1 < exp_2
    #
    # def visitLRA_In(self, ctx):
    #     exp = self.visit(ctx.expression(0))
    #     exp_low = self.visit(ctx.expression(1))
    #     exp_up = self.visit(ctx.expression(2))
    #     return And(exp_low < exp, exp < exp_up)
    #
    # def visitExpressionExponential(self, ctx):
    #     raise Exception('Exponents cannot be translated to Z3')
    #
    # def visitExpressionAddition(self, ctx):
    #     exp_1 = self.visit(ctx.expression(0))
    #     exp_2 = self.visit(ctx.expression(1))
    #     return exp_1 + exp_2
    #
    # def visitExpressionSubtraction(self, ctx):
    #     exp_1 = self.visit(ctx.expression(0))
    #     exp_2 = self.visit(ctx.expression(1))
    #     return exp_1 - exp_2
    #
    # def visitExpressionMultiplication(self, ctx):
    #     exp_1 = self.visit(ctx.expression(0))
    #     exp_2 = self.visit(ctx.expression(1))
    #     return exp_1 * exp_2
    #
    # def visitExpressionVariable(self, ctx):
    #     var_name = ctx.Identifier().getText()
    #     var = Real(var_name)
    #     return var
    #
    # def visitExpressionConstant(self, ctx):
    #     constant = RealVal(float(ctx.literal().getText()))
    #     return constant
    #
    # def visitExpressionParanthesis(self, ctx):
    #     return self.visit(ctx.expression())
