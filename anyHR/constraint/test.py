from ConstraintParser import Constraint2Tree

from antlr4.InputStream import InputStream
from antlr4.CommonTokenStream import CommonTokenStream
from constraint.parser.ConstraintLexer import ConstraintLexer
from constraint.parser.ConstraintParser import ConstraintParser


from node.Node import *


input = "a+b <= 4"

input_stream = InputStream(input)
lexer = ConstraintLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = ConstraintParser(stream)
ctx = parser.lra()

tree_parser = Constraint2Tree(ctx, ['a','b'])

testtree = tree_parser.return_tree()

print(testtree)