import math

from node.Node import *
from node.Visitor import NodeVisitor


class ConstraintEvaluator(NodeVisitor):
    """
    This class evaluates constraints to True or False and operations to their respective float values by substituting
    concrete values.
    """

    def __init__(self, ctx, var_name_list: list, node: Node):
        self.node = node
        self.ctx = ctx
        self.var_name_idx_dict = dict()
        self.sample = []

        # Create a dictionary mapping var names to array indices
        i = 0
        for var_name in var_name_list:
            self.var_name_idx_dict[var_name] = i
            i += 1

    def evaluate(self, sample: list) -> bool:
        self.sample = sample
        out = self.visit(self.node)
        return out

    def visitLEQ(self, node: LEQ, args) -> bool:
        exp_1 = self.visit(node.children[0])
        exp_2 = self.visit(node.children[1])
        return exp_1 <= exp_2

    def visitGEQ(self, node: GEQ, args) -> bool:
        exp_1 = self.visit(node.children[0])
        exp_2 = self.visit(node.children[1])
        return exp_1 >= exp_2

    def visitGreater(self, node: Greater, args) -> bool:
        exp_1 = self.visit(node.children[0])
        exp_2 = self.visit(node.children[1])
        return exp_1 > exp_2

    def visitLess(self, node: Less, args) -> bool:
        exp_1 = self.visit(node.children[0])
        exp_2 = self.visit(node.children[1])
        return exp_1 < exp_2

    def visitEQ(self, node: EQ, args) -> bool:
        exp_1 = self.visit(node.children[0])
        exp_2 = self.visit(node.children[1])
        return exp_1 == exp_2

    def visitNEQ(self, node: NEQ, args) -> bool:
        exp_1 = self.visit(node.children[0])
        exp_2 = self.visit(node.children[1])
        return exp_1 != exp_2

    def visitIn(self, node: In, args) -> bool:
        exp = self.visit(node.children[0])
        exp_low = self.visit(node.children[1])
        exp_up = self.visit(node.children[2])
        return exp_low < exp < exp_up

    def visitVariable(self, node: Variable, args) -> float:
        var_name = node.name
        idx = self.var_name_idx_dict[var_name]
        var = self.sample[idx]
        return var

    def visitConstant(self, node: Constant, args) -> float:
        constant = node.value
        return constant

    def visitAddition(self, ctx, node: Addition) -> float:
        exp_1 = self.visit(node.children[0])
        exp_2 = self.visit(node.children[1])
        return exp_1 + exp_2

    def visitExpressionSubtraction(self, node: Subtraction) -> float:
        exp_1 = self.visit(node.children[0])
        exp_2 = self.visit(node.children[1])
        return exp_1 - exp_2

    def visitExpressionMultiplication(self, node: Multiplication) -> float:
        exp_1 = self.visit(node.children[0])
        exp_2 = self.visit(node.children[1])
        return exp_1 * exp_2

    def visitExpressionExponential(self, node: Exponential) -> float:
        exp = self.visit(node.children[0])
        return math.exp(exp)

    # def visitExpressionParanthesis(self, ctx):
    #     return self.visit(ctx.expression())
