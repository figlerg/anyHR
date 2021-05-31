import math

from anyHR.constraint.node.Node import *
from anyHR.constraint.node.Visitor import NodeVisitor


class ConstraintEvaluator(NodeVisitor):
    """
    This class evaluates constraints in tree form (see Node.py) to True or False and operations to their respective
    float values by substituting concrete values. At this point we are independent from ANTLR4!
    """

    def __init__(self, node: Node, var_name_list: list):
        self.node = node
        self.var_name_idx_dict = dict()
        self.sample = []

        # Create a dictionary mapping var names to array indices
        i = 0
        for var_name in var_name_list:
            self.var_name_idx_dict[var_name] = i
            i += 1

    def evaluate(self, sample: list) -> bool:
        self.sample = sample
        out = self.visit(self.node, None)
        return out

    def visitLEQ(self, node: LEQ, args) -> bool:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 <= exp_2

    def visitGEQ(self, node: GEQ, args) -> bool:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 >= exp_2

    def visitGreater(self, node: Greater, args) -> bool:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 > exp_2

    def visitLess(self, node: Less, args) -> bool:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 < exp_2

    def visitEQ(self, node: EQ, args) -> bool:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 == exp_2

    def visitNEQ(self, node: NEQ, args) -> bool:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 != exp_2

    def visitIn(self, node: In, args) -> bool:
        exp = self.visit(node.children[0], args)
        exp_low = self.visit(node.children[1], args)
        exp_up = self.visit(node.children[2], args)
        return exp_low < exp < exp_up

    def visitVariable(self, node: Variable, args) -> float:
        var_name = node.name
        idx = self.var_name_idx_dict[var_name]
        var = self.sample[idx]
        return var

    def visitConstant(self, node: Constant, args) -> float:
        constant = node.value
        return constant

    def visitAddition(self, node: Addition, args) -> float:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 + exp_2

    def visitSubtraction(self, node: Subtraction, args) -> float:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 - exp_2

    def visitMultiplication(self, node: Multiplication, args) -> float:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 * exp_2

    def visitExponential(self, node: Exponential, args) -> float:
        exp = self.visit(node.children[0], args)
        return math.exp(exp)

    # def visitExpressionParanthesis(self, ctx):
    #     return self.visit(ctx.expression())
