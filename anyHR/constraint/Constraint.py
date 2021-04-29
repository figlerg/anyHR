from z3 import *
from antlr4.InputStream import InputStream
from antlr4.CommonTokenStream import CommonTokenStream

from anyHR.constraint.ConstraintQuantitativeEvaluator import ConstraintQuantitativeEvaluator
from anyHR.constraint.ConstrainttoZ3Equality import ConstrainttoZ3Equality
from anyHR.constraint.parser.ConstraintLexer import ConstraintLexer
from anyHR.constraint.parser.ConstraintParser import ConstraintParser
from anyHR.constraint.ConstrainttoZ3 import ConstrainttoZ3
from anyHR.constraint.ConstraintEvaluator import ConstraintEvaluator

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
        self.is_polynomial = True

    def add_constraint(self, constraint: str):
        # parse the constraint
        input_stream = InputStream(constraint)
        lexer = ConstraintLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ConstraintParser(stream)
        ctx = parser.lra()

        # Generate an evaluator for the specific constraint
        # and add it to the list
        evaluator = ConstraintEvaluator(ctx, self.var_name_list)
        self.c_evaluators.append(evaluator)

        # Generate a quantitative evaluator for the specific constraint
        # and add it to the list
        qevaluator = ConstraintQuantitativeEvaluator(ctx, self.var_name_list)
        self.c_qevaluators.append(qevaluator)

        try:
            # Generate a Z3 formula for the specific constraint
            # and add it to the list
            translator = ConstrainttoZ3(ctx)
            z3_formula = translator.translate()
            self.c_formulas.append(z3_formula)
            self.solver.add(z3_formula)

            # Generate a contour Z3 formula for the specific constraint
            # and add it to the list
            translator = ConstrainttoZ3Equality(ctx)
            z3_formula = translator.translate()
            self.c_contour_formulas.append(z3_formula)
        except Exception:
            self.is_polynomial = False

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


