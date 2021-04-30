from abc import ABCMeta, abstractmethod
from constraint.node.Node import *

NOT_IMPLEMENTED = "You should implement this."


class NodeVisitor:
    __metaclass__ = ABCMeta

    def visit(self, node, args):
        out = None

        if isinstance(node, LEQ):
            out = self.visitLEQ(node, args)
        elif isinstance(node, GEQ):
            out = self.visitGEQ(node, args)
        elif isinstance(node, Less):
            out = self.visitLess(node, args)
        elif isinstance(node, Greater):
            out = self.visitGreater(node, args)
        elif isinstance(node, EQ):
            out = self.visitEQ(node, args)
        elif isinstance(node, NEQ):
            out = self.visitNEQ(node, args)
        elif isinstance(node, In):
            out = self.visitIn(node, args)
        elif isinstance(node, Variable):
            out = self.visitVariable(node, args)
        elif isinstance(node, Constant):
            out = self.visitConstant(node, args)
        elif isinstance(node, Addition):
            out = self.visitAddition(node, args)
        elif isinstance(node, Subtraction):
            out = self.visitSubtraction(node, args)
        elif isinstance(node, Multiplication):
            out = self.visitMultiplication(node, args)
        elif isinstance(node, Exponential):
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