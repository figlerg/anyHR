from abc import ABCMeta, abstractmethod
from constraint.node.Node import *

NOT_IMPLEMENTED = "You should implement this."


class NodeVisitor:
    __metaclass__ = ABCMeta

    def visit(self, node, args):
        out = None

        if node.node_type ==  NodeType.LEQ:
            out = self.visitLEQ(node, args)
        elif node.node_type ==  NodeType.GEQ:
            out = self.visitGEQ(node, args)
        elif node.node_type ==  NodeType.LESS:
            out = self.visitLess(node, args)
        elif node.node_type ==  NodeType.GREATER:
            out = self.visitGreater(node, args)
        elif node.node_type ==  NodeType.EQ:
            out = self.visitEQ(node, args)
        elif node.node_type ==  NodeType.NEQ:
            out = self.visitNEQ(node, args)
        elif node.node_type ==  NodeType.IN:
            out = self.visitIn(node, args)
        elif node.node_type ==  NodeType.VARIABLE:
            out = self.visitVariable(node, args)
        elif node.node_type ==  NodeType.CONSTANT:
            out = self.visitConstant(node, args)
        elif node.node_type ==  NodeType.ADDITION:
            out = self.visitAddition(node, args)
        elif node.node_type ==  NodeType.SUBTRACTION:
            out = self.visitSubtraction(node, args)
        elif node.node_type ==  NodeType.MULTIPLICATION:
            out = self.visitMultiplication(node, args)
        elif node.node_type ==  NodeType.EXPONENTIAL:
            out = self.visitExponential(node, args)
        else:
            raise Exception('Node Visitor: unexpected method called.')
        return out

    @abstractmethod
    def visitLEQ(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitGEQ(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitLess(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitGreater(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitEQ(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitNEQ(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitIn(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitConstant(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitVariable(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitAddition(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitSubtraction(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitMultiplication(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitExponential(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)