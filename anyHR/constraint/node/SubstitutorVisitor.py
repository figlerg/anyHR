from typing import Dict

from constraint.node.Node import *
from constraint.node.Visitor import NodeVisitor


class SubstitutorVisitor(NodeVisitor):
    """
    This is a helper visitor which substitutes a variable node with a constant node
    """

    def __init__(self, node:Node):
        self.node = node
        self.pairs_dict = None


    def substitute(self,var_val_pairs: Dict[str, float]):
        self.pairs_dict = var_val_pairs
        self.visit(self.node, None)
        # this changes the node itself, no return value

    # this is the only interesting part:
    def visitVariable(self, node: Variable, args) -> float:
        for var in self.pairs_dict.keys():
            if node.name == var:
                # Transforms the variable node to a constant node
                node = Constant(self.pairs_dict[var])

                # no need to look further
                return

    def visitConstant(self, node: Constant, args) -> float:
        pass

    # the rest just visits all children
    def visitLEQ(self, node: LEQ, args) -> bool:
        for child in node.children:
            self.visit(child,None)

    def visitGEQ(self, node: GEQ, args) -> bool:
        for child in node.children:
            self.visit(child,None)

    def visitGreater(self, node: Greater, args) -> bool:
        for child in node.children:
            self.visit(child,None)

    def visitLess(self, node: Less, args) -> bool:
        for child in node.children:
            self.visit(child,None)

    def visitEQ(self, node: EQ, args) -> bool:
        for child in node.children:
            self.visit(child,None)

    def visitNEQ(self, node: NEQ, args) -> bool:
        for child in node.children:
            self.visit(child,None)

    def visitIn(self, node: In, args) -> bool:
        for child in node.children:
            self.visit(child,None)


    def visitAddition(self, node: Addition, args) -> float:
        for child in node.children:
            self.visit(child,None)

    def visitSubtraction(self, node: Subtraction, args) -> float:
        for child in node.children:
            self.visit(child,None)

    def visitMultiplication(self, node: Multiplication, args) -> float:
        for child in node.children:
            self.visit(child,None)

    def visitExponential(self, node: Exponential, args) -> float:
        for child in node.children:
            self.visit(child,None)