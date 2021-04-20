# Generated from C:/Users/giglerf/Desktop/anyHR/anyHR/constraint/grammar\ConstraintParser.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ConstraintParser import ConstraintParser
else:
    from ConstraintParser import ConstraintParser

# This class defines a complete generic visitor for a parse tree produced by ConstraintParser.

class ConstraintParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ConstraintParser#LRA_LEQ.
    def visitLRA_LEQ(self, ctx:ConstraintParser.LRA_LEQContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConstraintParser#LRA_GEQ.
    def visitLRA_GEQ(self, ctx:ConstraintParser.LRA_GEQContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConstraintParser#LRA_Less.
    def visitLRA_Less(self, ctx:ConstraintParser.LRA_LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConstraintParser#LRA_Greater.
    def visitLRA_Greater(self, ctx:ConstraintParser.LRA_GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConstraintParser#LRA_Eq.
    def visitLRA_Eq(self, ctx:ConstraintParser.LRA_EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConstraintParser#LRA_Neq.
    def visitLRA_Neq(self, ctx:ConstraintParser.LRA_NeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConstraintParser#LRA_In.
    def visitLRA_In(self, ctx:ConstraintParser.LRA_InContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConstraintParser#ExpressionParanthesis.
    def visitExpressionParanthesis(self, ctx:ConstraintParser.ExpressionParanthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConstraintParser#ExpressionMultiplication.
    def visitExpressionMultiplication(self, ctx:ConstraintParser.ExpressionMultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConstraintParser#ExpressionSubtraction.
    def visitExpressionSubtraction(self, ctx:ConstraintParser.ExpressionSubtractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConstraintParser#ExpressionAddition.
    def visitExpressionAddition(self, ctx:ConstraintParser.ExpressionAdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConstraintParser#ExpressionVariable.
    def visitExpressionVariable(self, ctx:ConstraintParser.ExpressionVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConstraintParser#ExpressionConstant.
    def visitExpressionConstant(self, ctx:ConstraintParser.ExpressionConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConstraintParser#ExpressionExponential.
    def visitExpressionExponential(self, ctx:ConstraintParser.ExpressionExponentialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConstraintParser#literal.
    def visitLiteral(self, ctx:ConstraintParser.LiteralContext):
        return self.visitChildren(ctx)



del ConstraintParser