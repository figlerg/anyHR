from enum import Enum
from scipy.spatial.distance import norm
from z3 import *
from pso.pso_ezio import *
from functools import partial
import numpy as np

def _obj_wrapper(func, args, kwargs, x):
    return func(x, *args, **kwargs)

class HRVariant(Enum):
    VANILLA = 0,
    SHRINKING = 1,
    SMT = 2,
    VANILLA_SMT = 3,
    SHRINKING_SMT = 4
    CDHR = 5

class DirectionSampling(Enum):
    RDHR = 0
    CDHR = 1

class Shrinking(Enum):
    NO_SHRINKING = 0
    SHRINKING = 1

class InitPoint(Enum):
    PSO = 0
    SMT = 1


class HitAndRun:
    def __init__(self, constraint, bounding_box, direction_sampling=DirectionSampling.RDHR,
                 shrinking=Shrinking.NO_SHRINKING, init_point=InitPoint.PSO):
        self.constraint = constraint
        self.bounding_box = bounding_box
        self.starting_point = self._starting_point()
        self.current_point = self.starting_point

        self.shrinking = shrinking
        self.direction_sampling = direction_sampling
        self.init_point = init_point


    def next_sample(self):
        if self.variant == HRVariant.VANILLA or self.variant == HRVariant.VANILLA_SMT:
            return self.next_sample_vanilla()
        elif self.variant == HRVariant.SHRINKING or self.variant == HRVariant.SHRINKING_SMT:
            return self.next_sample_with_shrinking()
        elif self.variant == HRVariant.CDHR:
            return self.next_sample_cdhr()
        else:
            return self.next_sample_z3()

    def next_sample_vanilla(self):
        b = self.current_point

        success = False
        while not success:
            a = self._random_direction()
            inter, success = self._line_box_intersection(a, b, self.bounding_box)

        success = False
        rejections = -1

        while not success:
            rnd = np.random.uniform()

            inter_1 = inter[0]
            inter_2 = inter[1]

            sample = []
            for i in range(len(inter_1)):
                x_0 = inter_1[i]
                x_1 = inter_2[i]
                s_i = (x_1 - x_0)*rnd + x_0
                sample.append(s_i)

            success = self.constraint.evaluate(sample)
            rejections += 1

        self.current_point = sample

        return sample, rejections

    def next_sample_z3(self):
        b = self.current_point
        counter = 0

        inter = []
        while not inter:
            a = self._random_direction()
            inter = self._line_S_intersection(a, b, self.constraint)
            counter = counter + 1

        success = False
        rejections = -1

        while not success:
            rnd = np.random.uniform()

            inter_1 = inter[0]
            inter_2 = inter[1]

            sample = []
            for i in range(len(inter_1)):
                x_0 = inter_1[i]
                x_1 = inter_2[i]
                s_i = (x_1 - x_0)*rnd + x_0
                sample.append(s_i)

            success = self.constraint.evaluate(sample)
            rejections += 1

        self.current_point = sample

        return sample, rejections

    def next_sample_with_shrinking(self):
        b = self.current_point

        success = False
        while not success:
            a = self._random_direction()
            inter, success = self._line_box_intersection(a, b, self.bounding_box)

        success = False
        rejections = -1

        inter_1 = inter[0]
        inter_2 = inter[1]

        r_1 = (inter_1[0] - b[0]) / a[0]
        r_2 = (inter_2[0] - b[0]) / a[0]
        r_min = min(r_1, r_2)
        r_max = max(r_1, r_2)

        while not success:
            rnd = np.random.uniform(r_min, r_max)

            sample = []
            for i in range(len(inter_1)):
                s_i = b[i] + rnd*a[i]
                sample.append(s_i)

            success = self.constraint.evaluate(sample)

            if not success:
                mid = r_min + 0.5*(r_max - r_min)
                if rnd > 0:
                    r_max = rnd
                else:
                    r_min = rnd


            rejections += 1

        # FELIX: fixed bug in next line, 30.03.
        self.current_point = sample

        return sample, rejections

    def next_sample_cdhr(self):
        b = self.current_point

        success = False
        while not success:
            a, direction_int = self._random_direction_cdhr()
            inter, success = self._line_box_intersection_cdhr(a, direction_int, b, self.bounding_box)

        success = False
        rejections = -1

        while not success:
            rnd = np.random.uniform()

            inter_1 = inter[0]
            inter_2 = inter[1]

            sample = []
            for i in range(len(inter_1)):
                x_0 = inter_1[i]
                x_1 = inter_2[i]
                s_i = (x_1 - x_0)*rnd + x_0
                sample.append(s_i)

            success = self.constraint.evaluate(sample)
            rejections += 1

        self.current_point = sample

        return sample, rejections


    def _line_box_intersection(self, a, b, box):
        potential_solutions = []
        for i in range(len(a)):
            box_i = box[i]
            box_i_min = box_i[0]
            box_i_max = box_i[1]
            t_min = (box_i_min - b[i]) / a[i]
            t_max = (box_i_max - b[i]) / a[i]
            potential_solutions.append(t_min)
            potential_solutions.append(t_max)

        solutions = []
        for ps in potential_solutions:
            is_solution = True
            solution = []
            for i in range(len(a)):
                box_i = box[i]
                result = a[i]*ps + b[i]
                solution.append(result)
                if result < box_i[0] or result > box_i[1]:
                    is_solution = False
                    break
            if is_solution:
                solutions.append(solution)


        if len(solutions) >= 2:
            flag = True
        else:
            flag = False

        return solutions, flag

    def _line_box_intersection_cdhr(self, a, direction_int, b, box):
        # this is much easier since we know in which dimensions the hyperplanes are hit
        potential_solutions = []

        # i = np.argmax(np.abs(a)) # where the 1 is (cdhr has only vectors (0,...,1,0,...,0))
        i = direction_int
        box_i = box[i]
        box_i_min = box_i[0]
        box_i_max = box_i[1]
        t_min = (box_i_min - b[i]) / a[i]
        t_max = (box_i_max - b[i]) / a[i]
        potential_solutions.append(t_min)
        potential_solutions.append(t_max)

        solutions = []
        for ps in potential_solutions:
            is_solution = True
            solution = a*ps + b
            solutions.append(solution)


        if len(solutions) >= 2:
            flag = True
        else:
            flag = False

        return solutions, flag

    # def contour(self):
    #     self.contur_solver = self.constraint.contour()

    # def _line_S_intersection(self, s0, s1, S):
    #     solver = self.constraint.contour()
    #     #solver.push()
    #
    #     for i in range(len(s0)):
    #         y0 = s0[i]
    #         y1 = s1[i]
    #         y = Real(S.var_name_list[i])
    #         if i == 0:
    #             x0 = s0[i]
    #             x1 = s1[i]
    #             x = Real(S.var_name_list[i])
    #         else:
    #             a = (y1-y0)/(x1-x0)
    #             b = y0 - a*x0
    #             a_str = '%.3f' % a
    #             b_str = '%.3f' % b
    #             a_smt = RealVal(a_str)
    #             b_smt = RealVal(b_str)
    #             constraint = y == a_smt*x + b_smt
    #             solver.add(constraint)
    #
    #     verdict = solver.check()
    #     solutions = []
    #     while verdict == sat:
    #         model = solver.model()
    #         for var in model:
    #             c = Real(str(var)) != model[var]
    #             solver.add(c)
    #
    #         solution = []
    #         for var_name in self.constraint.var_name_list:
    #             if isinstance(model[Real(var_name)], RatNumRef):
    #
    #                 val = float(model[Real(var_name)].as_fraction())
    #             else:
    #                 val = float(model[Real(var_name)].approx(self.precision).as_fraction())
    #             solution.append(val)
    #
    #         solutions.append(solution)
    #
    #         verdict = solver.check()
    #
    #     solutions.sort(key=self._sort_first)
    #     #solver.pop()
    #
    #     return solutions
    #
    # def _line_S_intersection_old(self, s0, s1, S):
    #     solver = self.contur_solver
    #     solver.push()
    #
    #     for i in range(len(s0)):
    #         v0 = '%.3f' % s0[i]
    #         v1 = '%.3f' % s1[i]
    #         v0 = RealVal(v0)
    #         v1 = RealVal(v1)
    #         x = Real(S.var_name_list[i])
    #         if i == 0:
    #             x0 = v0
    #             x1 = v1
    #             tmp = RealVal(1)/(v1-v0)
    #             t = (x - v0)*tmp
    #         else:
    #             tmp = RealVal(1)/(x1-x0)
    #             y = x == ((v1 - v0)*(t - x0))*tmp + v0
    #             solver.add(y)
    #
    #     verdict = solver.check()
    #     solutions = []
    #     while verdict == sat:
    #         model = solver.model()
    #         for var in model:
    #             c = Real(str(var)) != model[var]
    #             solver.add(c)
    #
    #         solution = []
    #         for var_name in self.constraint.var_name_list:
    #             val = float(model[Real(var_name)].approx(self.precision).as_fraction())
    #             solution.append(val)
    #
    #         solutions.append(solution)
    #
    #         verdict = solver.check()
    #
    #     solutions.sort(key=self._sort_first)
    #     solver.pop()
    #
    #     return solutions

    def _sort_first(self, l):
        return l[0]

    def _starting_point(self):
        if self.variant == HRVariant.SMT or self.variant == HRVariant.SHRINKING_SMT or self.variant == HRVariant.VANILLA_SMT or self.variant == HRVariant.CDHR:
            return self._starting_point_smt()
        else:
            return self._starting_point_pso()

    def _starting_point_pso(self):

        lb = []
        ub = []
        for b in self.bounding_box:
            lb.append(b[0])
            ub.append(b[1])

        #out, rob_opt = pso(self._evaluate, lb, ub, f_ieqcons=None, swarmsize=10, omega=0.5, phip=0.5,
        #                   phig=0.5, maxiter=10, minstep=1e-2, minfunc=0.1, debug=False)

        out, rob_opt, budget = pso(self._evaluate, lb, ub, f_ieqcons=None, swarmsize=10000, omega=0.5, phip=0.5,
                                   phig=0.5, maxiter=10000, minstep=1e-2, minfunc=0.1, debug=False)

        if rob_opt > 0:
            raise Exception('Could not find a starting point in the set.')

        return out

    def _evaluate(self, sample):
        return -self.constraint.q_evaluate(sample)


    def _starting_point_smt(self):
        solver = self.constraint.solver
        status = solver.check()

        if status == unsat:
            raise Exception('The set of constraints is unsatisfiable.')

        model = solver.model()

        out_d = dict()
        for var in model:
            value = model[var]
            num = float(value.numerator_as_long())
            den = float(value.denominator_as_long())
            out_d[str(var)] = num/den

        out = []
        for var in self.constraint.var_name_list:
            out.append(out_d[var])

        return out

    def _random_direction(self):
        direction = []
        for i in range(self.constraint.dimensions):
            dir = np.random.uniform(-1, 1)
            direction.append(dir)
        direction = np.array(direction)
        direction = direction / norm(direction)
        return direction

    def optimize(self, func, threshold=-np.inf, maxiter=100, minfunc=1e-8, args=(), kwargs={}):
        """
        Perform the minimization of the objective function 'func' under the constraints stored in self.S
        NOTE: This method can only be invoked after 'self' is initialized which requires itself some optimization
        method, e.g. pso(), in order to initialize self.starting_point.

        Parameters
        ==========
        func : function
            The function to be minimized

        Optional
        ========
        threshold : scalar
            The algorithm will try to minimize the objective function to a value
            which is less than the value specified in 'threshold'
            (Default: -np.inf)
        maxiter : int
            The maximum number of iterations for the swarm to search
            (Default: 100)
        minfunc : scalar
            The minimum change of swarm's best objective value before the search terminates
            (Default: 1e-8)
        args : tuple
            Additional arguments passed to objective and constraint functions
            (Default: empty tuple)
        kwargs : dict
            Additional keyword arguments passed to objective and constraint
            functions (Default: empty dict)

        Returns
        =======
        x : array
            The best sample (optimal design)
        f : scalar
            The objective value at ``x``
        i: int
            The remaining number of iterations which were not used

        """

        # Initialize objective function
        obj = partial(_obj_wrapper, func, args, kwargs)

        x = self.current_point
        fx = obj(x)

        if fx < threshold:
            print('Stopping search: objective below threshold ({}) already at the starting point' \
                  .format(threshold))
            return x, fx, maxiter

        # Iterate until termination criterion met
        it = 1
        while it <= maxiter:
            z, _ = self.next_sample()   # this will set also self.current_point = z
            print('Iteration ' + str(it))
            fz = obj(z)

            if fz < fx:
                if np.abs(fx - fz) <= minfunc:
                    print('Stopping search: objective change less than {:}'.format(minfunc))
                    return z, fz, maxiter - it
                if fz < threshold:
                    print('Stopping search: objective below threshold ({})'.format(threshold))
                    return z, fz, maxiter - it
                x = z
                fx = fz
            else:
                # current_point rollback:
                self.current_point = x

            it += 1

        print('Stopping search: maximum iterations reached --> {:}'.format(maxiter))

        return x, fx, 0

    def _random_direction_cdhr(self):
        n = self.constraint.dimensions

        sign = np.random.rand() < 0.5 # random bit
        direction = np.random.randint(low=0, high=n)

        out = np.zeros(n)
        out[direction] = 1

        if sign:
            pass # plus
        else:
            out[direction] *= -1 # minus

        return out, direction
        # here I return direction, seems like unnecessary extra steps to compute argmax in next_sample_cdhr
