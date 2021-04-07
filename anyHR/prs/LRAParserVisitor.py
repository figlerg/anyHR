# Generated from LRAParser.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LRAParser import LRAParser
else:
    from LRAParser import LRAParser

# This class defines a complete generic visitor for a parse tree produced by LRAParser.

class LRAParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LRAParser#LRA_LEQ.
    def visitLRA_LEQ(self, ctx:LRAParser.LRA_LEQContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LRAParser#LRA_GEQ.
    def visitLRA_GEQ(self, ctx:LRAParser.LRA_GEQContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LRAParser#LRA_Less.
    def visitLRA_Less(self, ctx:LRAParser.LRA_LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LRAParser#LRA_Greater.
    def visitLRA_Greater(self, ctx:LRAParser.LRA_GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LRAParser#LRA_Eq.
    def visitLRA_Eq(self, ctx:LRAParser.LRA_EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LRAParser#LRA_Neq.
    def visitLRA_Neq(self, ctx:LRAParser.LRA_NeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LRAParser#LRA_In.
    def visitLRA_In(self, ctx:LRAParser.LRA_InContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LRAParser#ExpressionParanthesis.
    def visitExpressionParanthesis(self, ctx:LRAParser.ExpressionParanthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LRAParser#ExpressionMultiplication.
    def visitExpressionMultiplication(self, ctx:LRAParser.ExpressionMultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LRAParser#ExpressionSubtraction.
    def visitExpressionSubtraction(self, ctx:LRAParser.ExpressionSubtractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LRAParser#ExpressionAddition.
    def visitExpressionAddition(self, ctx:LRAParser.ExpressionAdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LRAParser#ExpressionVariable.
    def visitExpressionVariable(self, ctx:LRAParser.ExpressionVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LRAParser#ExpressionExponential.
    def visitExpressionExponential(self, ctx:LRAParser.ExpressionExponentialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LRAParser#ExpressionConstant.
    def visitExpressionConstant(self, ctx:LRAParser.ExpressionConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LRAParser#literal.
    def visitLiteral(self, ctx:LRAParser.LiteralContext):
        return self.visitChildren(ctx)



del LRAParser