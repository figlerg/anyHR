from z3 import *
from antlr4.InputStream import InputStream
from antlr4.CommonTokenStream import CommonTokenStream

from constraint.LRAQuantitativeEvaluator import LRAQuantitativeEvaluator
from constraint.LRAtoZ3Equality import LRAtoZ3Equality
from prs.LRALexer import LRALexer
from prs.LRAParser import LRAParser
from constraint.LRAtoZ3 import LRAtoZ3
from constraint.LRAEvaluator import LRAEvaluator

class Constraints:
    """
    Class encoding a set of NLRA constraint
    """
    def __init__(self, var_name_list: list):
        self.var_name_list = var_name_list      # list of variables used in the set of constraint
        self.solver = Solver()                  # instance of the Z3 solver
        self.c_evaluators = []                  # list of constraint evaluators
        self.c_qevaluators = []                 # list of constraint quantitative evaluators
        self.c_formulas = []                    # list of constraint Z3 formulas
        self.c_contour_formulas = []            # list of contour constraint Z3 formulas
        self.dimensions = len(var_name_list)    # nb of dimensions

    def add_constraint(self, constraint: str):
        # parse the constraint
        input_stream = InputStream(constraint)
        lexer = LRALexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = LRAParser(stream)
        ctx = parser.lra()

        # Generate an evaluator for the specific constraint
        # and add it to the list
        evaluator = LRAEvaluator(ctx, self.var_name_list)
        self.c_evaluators.append(evaluator)

        # Generate a quantitative evaluator for the specific constraint
        # and add it to the list
        qevaluator = LRAQuantitativeEvaluator(ctx, self.var_name_list)
        self.c_qevaluators.append(qevaluator)

        # Generate a Z3 formula for the specific constraint
        # and add it to the list
        translator = LRAtoZ3(ctx)
        z3_formula = translator.translate()
        self.c_formulas.append(z3_formula)
        self.solver.add(z3_formula)

        # Generate a contour Z3 formula for the specific constraint
        # and add it to the list
        translator = LRAtoZ3Equality(ctx)
        z3_formula = translator.translate()
        self.c_contour_formulas.append(z3_formula)


    def evaluate(self, sample: list):
        """
        Evaluates whether the sample satisfies or violates the set of constraint
        :param sample: n-dimensional list of floats, ex. [2.3, 1.2, 3.3]
        :return: bool
        """
        out = True
        for evaluator in self.c_evaluators:
            out = out and evaluator.evaluate(sample)
        return out

    def q_evaluate(self, sample: list):
        """
        Quantitatively evaluates whether the sample satisfies or violates the set of constraint
        :param sample: n-dimensional list of floats, ex. [2.3, 1.2, 3.3]
        :return: scalar
        """
        out = float("inf")
        for qevaluator in self.c_qevaluators:
            out = min(out, qevaluator.evaluate(sample))
        return out

    def q_evaluate_args(self, sample: list, *args : list):
        """
        Quantitatively evaluates whether the sample satisfies or violates the set of constraint
        :param sample: n-dimensional list of floats, ex. [2.3, 1.2, 3.3]
        :return: scalar
        """
        out = float("inf")
        for qevaluator in self.c_qevaluators:
            out = min(out, qevaluator.evaluate(sample))
        return out

    def f_ieqcons(self, sample: list):
        """
        Returns a list containing the quantitative evaluations of the constraints. A constraint is
        satisfied when its quantitative evaluation is greater or equal to 0.
        :param sample: n-dimensional list of floats, ex. [2.3, 1.2, 3.3]
        :return: list of scalars
        """
        out = []
        for qevaluator in self.c_qevaluators:
            out.append(qevaluator.evaluate(sample))
        return out

    def contour(self):
        solver = Solver()
        for i in range(len(self.c_formulas)):
            for j in range(len(self.c_formulas)):
                if not i == j:
                    formula = self.c_formulas[j]
                else:
                    formula = self.c_contour_formulas[j]
                if j == 0:
                    current = formula
                else:
                    current = And(current, formula)
            if i == 0:
                top_current = current
            else:
                top_current = Or(top_current, current)
        solver.add(top_current)
        return solver



    @property
    def solver(self):
        return self.__solver

    @solver.setter
    def solver(self, solver):
        self.__solver = solver

    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        self.__dimensions = dimensions


