from typing import Dict

from anyHR.constraint.node.Node import *
from anyHR.constraint.node.Visitor import NodeVisitor


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
    def visitVariable(self, node: Variable, args):
        raise Exception('This should be unreachable.')

    def visitConstant(self, node: Constant, args):
        pass

    # checks whether child is variable and whether we have a value for it
    def substitute_children(self, node):
        for i, child in enumerate(node.children):
            if child.node_type == NodeType.VARIABLE:
                if child.name in self.pairs_dict.keys():
                    node.children[i] = Constant(self.pairs_dict[child.name]) # overwrites variable node with constant node
            else:
                self.visit(child,None)

    # the rest visits children or substitutes variable children
    def visitLEQ(self, node: LEQ, args):
        self.substitute_children(node)

    def visitGEQ(self, node: GEQ, args):
        self.substitute_children(node)

    def visitGreater(self, node: Greater, args):
        self.substitute_children(node)

    def visitLess(self, node: Less, args):
        self.substitute_children(node)

    def visitEQ(self, node: EQ, args):
        self.substitute_children(node)

    def visitNEQ(self, node: NEQ, args):
        self.substitute_children(node)

    def visitIn(self, node: In, args):
        self.substitute_children(node)


    def visitAddition(self, node: Addition, args):
        self.substitute_children(node)

    def visitSubtraction(self, node: Subtraction, args):
        self.substitute_children(node)

    def visitMultiplication(self, node: Multiplication, args):
        self.substitute_children(node)

    def visitExponential(self, node: Exponential, args):
        self.substitute_children(node)

