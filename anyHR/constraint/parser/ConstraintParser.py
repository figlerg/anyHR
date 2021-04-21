# Generated from C:/Users/giglerf/Desktop/anyHR/anyHR/constraint/grammar\ConstraintParser.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32")
        buf.write("K\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2)\n")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\65\n\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3@\n\3\f\3\16\3")
        buf.write("C\13\3\3\4\3\4\3\4\3\4\5\4I\n\4\3\4\2\3\4\5\2\4\6\2\2")
        buf.write("\2U\2(\3\2\2\2\4\64\3\2\2\2\6H\3\2\2\2\b\t\5\4\3\2\t\n")
        buf.write("\7\f\2\2\n\13\5\4\3\2\13)\3\2\2\2\f\r\5\4\3\2\r\16\7\r")
        buf.write("\2\2\16\17\5\4\3\2\17)\3\2\2\2\20\21\5\4\3\2\21\22\7\16")
        buf.write("\2\2\22\23\5\4\3\2\23)\3\2\2\2\24\25\5\4\3\2\25\26\7\17")
        buf.write("\2\2\26\27\5\4\3\2\27)\3\2\2\2\30\31\5\4\3\2\31\32\7\20")
        buf.write("\2\2\32\33\5\4\3\2\33)\3\2\2\2\34\35\5\4\3\2\35\36\7\21")
        buf.write("\2\2\36\37\5\4\3\2\37)\3\2\2\2 !\5\4\3\2!\"\7\23\2\2\"")
        buf.write("#\7\b\2\2#$\5\4\3\2$%\7\22\2\2%&\5\4\3\2&\'\7\t\2\2\'")
        buf.write(")\3\2\2\2(\b\3\2\2\2(\f\3\2\2\2(\20\3\2\2\2(\24\3\2\2")
        buf.write("\2(\30\3\2\2\2(\34\3\2\2\2( \3\2\2\2)\3\3\2\2\2*+\b\3")
        buf.write("\1\2+\65\7\26\2\2,\65\5\6\4\2-.\7\b\2\2./\5\4\3\2/\60")
        buf.write("\7\t\2\2\60\65\3\2\2\2\61\62\7\3\2\2\62\63\7\4\2\2\63")
        buf.write("\65\5\4\3\6\64*\3\2\2\2\64,\3\2\2\2\64-\3\2\2\2\64\61")
        buf.write("\3\2\2\2\65A\3\2\2\2\66\67\f\5\2\2\678\7\7\2\28@\5\4\3")
        buf.write("\69:\f\4\2\2:;\7\6\2\2;@\5\4\3\5<=\f\3\2\2=>\7\5\2\2>")
        buf.write("@\5\4\3\4?\66\3\2\2\2?9\3\2\2\2?<\3\2\2\2@C\3\2\2\2A?")
        buf.write("\3\2\2\2AB\3\2\2\2B\5\3\2\2\2CA\3\2\2\2DI\7\24\2\2EI\7")
        buf.write("\25\2\2FG\7\5\2\2GI\5\6\4\2HD\3\2\2\2HE\3\2\2\2HF\3\2")
        buf.write("\2\2I\7\3\2\2\2\7(\64?AH")
        return buf.getvalue()


class ConstraintParser ( Parser ):

    grammarFileName = "ConstraintParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'e'", "'**'", "'-'", "'+'", "'*'", "'('", 
                     "')'", "'['", "']'", "'<='", "'>='", "'<'", "'>'", 
                     "'=='", "'!='", "','", "'in'" ]

    symbolicNames = [ "<INVALID>", "EULER", "EXP", "MINUS", "PLUS", "TIMES", 
                      "LPAREN", "RPAREN", "LSQBRACKET", "RSQBRACKET", "LEQ", 
                      "GEQ", "LESS", "GREATER", "EQ", "NEQ", "COMMA", "IN", 
                      "IntegerLiteral", "RealLiteral", "Identifier", "LINE_TERMINATOR", 
                      "WHITESPACE", "COMMENT", "LINE_COMMENT" ]

    RULE_lra = 0
    RULE_expression = 1
    RULE_literal = 2

    ruleNames =  [ "lra", "expression", "literal" ]

    EOF = Token.EOF
    EULER=1
    EXP=2
    MINUS=3
    PLUS=4
    TIMES=5
    LPAREN=6
    RPAREN=7
    LSQBRACKET=8
    RSQBRACKET=9
    LEQ=10
    GEQ=11
    LESS=12
    GREATER=13
    EQ=14
    NEQ=15
    COMMA=16
    IN=17
    IntegerLiteral=18
    RealLiteral=19
    Identifier=20
    LINE_TERMINATOR=21
    WHITESPACE=22
    COMMENT=23
    LINE_COMMENT=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ConstraintParser.RULE_lra

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LRA_NeqContext(LraContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConstraintParser.LraContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConstraintParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ConstraintParser.ExpressionContext,i)

        def NEQ(self):
            return self.getToken(ConstraintParser.NEQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLRA_Neq" ):
                return visitor.visitLRA_Neq(self)
            else:
                return visitor.visitChildren(self)


    class LRA_EqContext(LraContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConstraintParser.LraContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConstraintParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ConstraintParser.ExpressionContext,i)

        def EQ(self):
            return self.getToken(ConstraintParser.EQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLRA_Eq" ):
                return visitor.visitLRA_Eq(self)
            else:
                return visitor.visitChildren(self)


    class LRA_LEQContext(LraContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConstraintParser.LraContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConstraintParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ConstraintParser.ExpressionContext,i)

        def LEQ(self):
            return self.getToken(ConstraintParser.LEQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLRA_LEQ" ):
                return visitor.visitLRA_LEQ(self)
            else:
                return visitor.visitChildren(self)


    class LRA_GEQContext(LraContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConstraintParser.LraContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConstraintParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ConstraintParser.ExpressionContext,i)

        def GEQ(self):
            return self.getToken(ConstraintParser.GEQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLRA_GEQ" ):
                return visitor.visitLRA_GEQ(self)
            else:
                return visitor.visitChildren(self)


    class LRA_InContext(LraContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConstraintParser.LraContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConstraintParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ConstraintParser.ExpressionContext,i)

        def IN(self):
            return self.getToken(ConstraintParser.IN, 0)
        def LPAREN(self):
            return self.getToken(ConstraintParser.LPAREN, 0)
        def COMMA(self):
            return self.getToken(ConstraintParser.COMMA, 0)
        def RPAREN(self):
            return self.getToken(ConstraintParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLRA_In" ):
                return visitor.visitLRA_In(self)
            else:
                return visitor.visitChildren(self)


    class LRA_GreaterContext(LraContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConstraintParser.LraContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConstraintParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ConstraintParser.ExpressionContext,i)

        def GREATER(self):
            return self.getToken(ConstraintParser.GREATER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLRA_Greater" ):
                return visitor.visitLRA_Greater(self)
            else:
                return visitor.visitChildren(self)


    class LRA_LessContext(LraContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConstraintParser.LraContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConstraintParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ConstraintParser.ExpressionContext,i)

        def LESS(self):
            return self.getToken(ConstraintParser.LESS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLRA_Less" ):
                return visitor.visitLRA_Less(self)
            else:
                return visitor.visitChildren(self)



    def lra(self):

        localctx = ConstraintParser.LraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_lra)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = ConstraintParser.LRA_LEQContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.expression(0)
                self.state = 7
                self.match(ConstraintParser.LEQ)
                self.state = 8
                self.expression(0)
                pass

            elif la_ == 2:
                localctx = ConstraintParser.LRA_GEQContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 10
                self.expression(0)
                self.state = 11
                self.match(ConstraintParser.GEQ)
                self.state = 12
                self.expression(0)
                pass

            elif la_ == 3:
                localctx = ConstraintParser.LRA_LessContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 14
                self.expression(0)
                self.state = 15
                self.match(ConstraintParser.LESS)
                self.state = 16
                self.expression(0)
                pass

            elif la_ == 4:
                localctx = ConstraintParser.LRA_GreaterContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 18
                self.expression(0)
                self.state = 19
                self.match(ConstraintParser.GREATER)
                self.state = 20
                self.expression(0)
                pass

            elif la_ == 5:
                localctx = ConstraintParser.LRA_EqContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 22
                self.expression(0)
                self.state = 23
                self.match(ConstraintParser.EQ)
                self.state = 24
                self.expression(0)
                pass

            elif la_ == 6:
                localctx = ConstraintParser.LRA_NeqContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 26
                self.expression(0)
                self.state = 27
                self.match(ConstraintParser.NEQ)
                self.state = 28
                self.expression(0)
                pass

            elif la_ == 7:
                localctx = ConstraintParser.LRA_InContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 30
                self.expression(0)
                self.state = 31
                self.match(ConstraintParser.IN)
                self.state = 32
                self.match(ConstraintParser.LPAREN)
                self.state = 33
                self.expression(0)
                self.state = 34
                self.match(ConstraintParser.COMMA)
                self.state = 35
                self.expression(0)
                self.state = 36
                self.match(ConstraintParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ConstraintParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExpressionParanthesisContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConstraintParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ConstraintParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(ConstraintParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(ConstraintParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionParanthesis" ):
                return visitor.visitExpressionParanthesis(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionMultiplicationContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConstraintParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConstraintParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ConstraintParser.ExpressionContext,i)

        def TIMES(self):
            return self.getToken(ConstraintParser.TIMES, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionMultiplication" ):
                return visitor.visitExpressionMultiplication(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionSubtractionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConstraintParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConstraintParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ConstraintParser.ExpressionContext,i)

        def MINUS(self):
            return self.getToken(ConstraintParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionSubtraction" ):
                return visitor.visitExpressionSubtraction(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionAdditionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConstraintParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConstraintParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ConstraintParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(ConstraintParser.PLUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionAddition" ):
                return visitor.visitExpressionAddition(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionVariableContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConstraintParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(ConstraintParser.Identifier, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionVariable" ):
                return visitor.visitExpressionVariable(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionConstantContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConstraintParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(ConstraintParser.LiteralContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionConstant" ):
                return visitor.visitExpressionConstant(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionExponentialContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConstraintParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EULER(self):
            return self.getToken(ConstraintParser.EULER, 0)
        def EXP(self):
            return self.getToken(ConstraintParser.EXP, 0)
        def expression(self):
            return self.getTypedRuleContext(ConstraintParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionExponential" ):
                return visitor.visitExpressionExponential(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ConstraintParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ConstraintParser.Identifier]:
                localctx = ConstraintParser.ExpressionVariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 41
                self.match(ConstraintParser.Identifier)
                pass
            elif token in [ConstraintParser.MINUS, ConstraintParser.IntegerLiteral, ConstraintParser.RealLiteral]:
                localctx = ConstraintParser.ExpressionConstantContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 42
                self.literal()
                pass
            elif token in [ConstraintParser.LPAREN]:
                localctx = ConstraintParser.ExpressionParanthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 43
                self.match(ConstraintParser.LPAREN)
                self.state = 44
                self.expression(0)
                self.state = 45
                self.match(ConstraintParser.RPAREN)
                pass
            elif token in [ConstraintParser.EULER]:
                localctx = ConstraintParser.ExpressionExponentialContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 47
                self.match(ConstraintParser.EULER)
                self.state = 48
                self.match(ConstraintParser.EXP)
                self.state = 49
                self.expression(4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 61
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = ConstraintParser.ExpressionMultiplicationContext(self, ConstraintParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 52
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 53
                        self.match(ConstraintParser.TIMES)
                        self.state = 54
                        self.expression(4)
                        pass

                    elif la_ == 2:
                        localctx = ConstraintParser.ExpressionAdditionContext(self, ConstraintParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 55
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 56
                        self.match(ConstraintParser.PLUS)
                        self.state = 57
                        self.expression(3)
                        pass

                    elif la_ == 3:
                        localctx = ConstraintParser.ExpressionSubtractionContext(self, ConstraintParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 58
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 59
                        self.match(ConstraintParser.MINUS)
                        self.state = 60
                        self.expression(2)
                        pass

             
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(ConstraintParser.IntegerLiteral, 0)

        def RealLiteral(self):
            return self.getToken(ConstraintParser.RealLiteral, 0)

        def MINUS(self):
            return self.getToken(ConstraintParser.MINUS, 0)

        def literal(self):
            return self.getTypedRuleContext(ConstraintParser.LiteralContext,0)


        def getRuleIndex(self):
            return ConstraintParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ConstraintParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_literal)
        try:
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ConstraintParser.IntegerLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(ConstraintParser.IntegerLiteral)
                pass
            elif token in [ConstraintParser.RealLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(ConstraintParser.RealLiteral)
                pass
            elif token in [ConstraintParser.MINUS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.match(ConstraintParser.MINUS)
                self.state = 69
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




