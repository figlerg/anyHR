from Constraint2Tree import Constraint2Tree

from antlr4.InputStream import InputStream
from antlr4.CommonTokenStream import CommonTokenStream
from constraint.parser.ConstraintLexer import ConstraintLexer
from constraint.parser.ConstraintParser import ConstraintParser
from constraint.ConstraintEvaluator import ConstraintEvaluator
from constraint.ConstraintQuantitativeEvaluator import ConstraintQuantitativeEvaluator

from constraint.ConstrainttoZ3 import ConstrainttoZ3
from constraint.ConstrainttoZ3Equality import ConstrainttoZ3Equality


from constraint.node.Node import *


input = "a+b <= 4"

input_stream = InputStream(input)
lexer = ConstraintLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = ConstraintParser(stream)
ctx = parser.lra()

tree_parser = Constraint2Tree(ctx, ['a','b'])

testtree = tree_parser.translate()
# testleq = LEQ(testtree,testtree)
# print('testleq:')
# print(type(testleq))
# print('actual tree:')
# print(type(testtree))
# print(isinstance(testtree, LEQ))

testevaluator = ConstraintEvaluator(['a','b'], testtree)
print('testevaluator api:')
print(testevaluator.evaluate([1,3.1]))
print('testevaluator quantitative api:')
testevaluatorquant = ConstraintQuantitativeEvaluator(['a','b'], testtree)
print(testevaluatorquant.evaluate([1,3.1]))

testz3evaluator = ConstrainttoZ3(testtree)
print('z3 object:')
print(testz3evaluator.translate())


testz3evaluatorequality = ConstrainttoZ3Equality(testtree)
print('z3 equality object:')
print(testz3evaluatorequality.translate())