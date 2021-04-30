from z3 import *

from constraint.node.Node import *
from constraint.node.Visitor import NodeVisitor


class ConstrainttoZ3Equality(NodeVisitor):
    '''
    This class translates the constraint tree to its Z3 representation
    '''

    def __init__(self, node: Node):
        self.node = node

    # api
    def translate(self):
        """Returns the Z3 translation of the NLRA constraint"""
        return self.visit(self.node, None)

    def visitLEQ(self, node: LEQ, args) -> bool:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 == exp_2

    def visitGEQ(self, node: GEQ, args) -> bool:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 == exp_2

    def visitGreater(self, node: Greater, args) -> bool:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 == exp_2

    def visitLess(self, node: Less, args) -> bool:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 == exp_2

    def visitEQ(self, node: EQ, args) -> bool:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 == exp_2

    def visitNEQ(self, node: NEQ, args) -> bool:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 == exp_2

    def visitIn(self, node: In, args) -> bool:
        exp = self.visit(node.children[0], args)
        exp_low = self.visit(node.children[1], args)
        exp_up = self.visit(node.children[2], args)
        return Or(exp_low == exp, exp == exp_up)

    def visitVariable(self, node: Variable, args) -> float:
        var_name = node.name
        var = Real(var_name)

        return var

    def visitConstant(self, node: Constant, args) -> float:
        constant = RealVal(node.value)
        return constant

    def visitAddition(self, node: Addition, args) -> float:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 + exp_2

    def visitExpressionSubtraction(self, node: Subtraction, args) -> float:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 - exp_2

    def visitExpressionMultiplication(self, node: Multiplication, args) -> float:
        exp_1 = self.visit(node.children[0], args)
        exp_2 = self.visit(node.children[1], args)
        return exp_1 * exp_2

    def visitExpressionExponential(self, node: Exponential, args):
        exp = self.visit(node.children[0], args)
        raise Exception('Exponentials cannot be translated to Z3')




