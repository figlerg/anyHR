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

    def visitLEQ(self, node: LEQ, args) -> ExprRef:
        exp_1:ExprRef = self.visit(node.children[0], args)
        exp_2:ExprRef = self.visit(node.children[1], args)
        return exp_1 == exp_2

    def visitGEQ(self, node: GEQ, args) -> ExprRef:
        exp_1:ExprRef = self.visit(node.children[0], args)
        exp_2:ExprRef = self.visit(node.children[1], args)
        return exp_1 == exp_2

    def visitGreater(self, node: Greater, args) -> ExprRef:
        exp_1:ExprRef = self.visit(node.children[0], args)
        exp_2:ExprRef = self.visit(node.children[1], args)
        return exp_1 == exp_2

    def visitLess(self, node: Less, args) -> ExprRef:
        exp_1:ExprRef = self.visit(node.children[0], args)
        exp_2:ExprRef = self.visit(node.children[1], args)
        return exp_1 == exp_2

    def visitEQ(self, node: EQ, args) -> ExprRef:
        exp_1:ExprRef = self.visit(node.children[0], args)
        exp_2:ExprRef = self.visit(node.children[1], args)
        return exp_1 == exp_2

    def visitNEQ(self, node: NEQ, args) -> ExprRef:
        exp_1:ExprRef = self.visit(node.children[0], args)
        exp_2:ExprRef = self.visit(node.children[1], args)
        return exp_1 == exp_2

    def visitIn(self, node: In, args) -> ExprRef:
        exp = self.visit(node.children[0], args)
        exp_low = self.visit(node.children[1], args)
        exp_up = self.visit(node.children[2], args)
        return Or(exp_low == exp, exp == exp_up)

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




