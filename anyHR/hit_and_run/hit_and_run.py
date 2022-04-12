from enum import Enum
from functools import partial

from z3 import *

from anyHR.constraint.Constraint import Constraints
from anyHR.pso.pso import *
import numpy as np


def _obj_wrapper(func, args, kwargs, x):
    return func(x, *args, **kwargs)


# class HRVariant(Enum):
#     VANILLA = 0,
#     SHRINKING = 1,
#     SMT = 2,
#     VANILLA_SMT = 3,
#     SHRINKING_SMT = 4
#     CDHR = 5


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
        self.shrinking = shrinking
        self.direction_sampling = direction_sampling
        self.init_point = init_point

        assert(self.init_point == InitPoint.PSO or self.constraint.is_polynomial), \
            "You cannot use non-polynomial constraints with SMT"


        # addition 12.04.2022, Felix: add constraints from box to the constraint object automatically
        #  otherwise the initial point may be outside for the smt modes, since it does not check for those
        variables = self.constraint.var_name_list
        for i,var in enumerate(variables):
            self.constraint.add_constraint(var + '>' + str(bounding_box[i][0]))
            self.constraint.add_constraint(var + '<' + str(bounding_box[i][1]))



        # set the starting point- either with optimizer or with smt solver
        if init_point == InitPoint.PSO:
            self.starting_point = self._starting_point_pso()
        else:  # using z3/SMT
            self.starting_point = self._starting_point_smt()

        self.current_point = self.starting_point

        # set the function handles according to the options (direction set, shrinking)
        #  Beware: the next_sample() function is being set here. This means
        if direction_sampling == DirectionSampling.RDHR and shrinking == Shrinking.NO_SHRINKING:  # simple RDHR
            self.next_sample = self._next_sample_vanilla
        elif direction_sampling == DirectionSampling.RDHR and shrinking == Shrinking.SHRINKING:  # RDHR + Shrinking
            self.next_sample = self._next_sample_rdhr_shrinking
        elif direction_sampling == DirectionSampling.CDHR and shrinking == Shrinking.NO_SHRINKING:  # simple CDHR
            self.next_sample = self._next_sample_cdhr
        elif direction_sampling == DirectionSampling.CDHR and shrinking == Shrinking.SHRINKING:
            self.next_sample = self.next_sample_cdhr_shrinking

    def sampler(self, n, burn_in_period=100):
        # should be the easiest way to get a sample- simple wrapper which needs little to none of the smaller methods

        dim = len(self.constraint.var_name_list)

        # start = time.perf_counter()

        samples = np.ndarray((dim, n))
        rejections = 0

        for i in range(n):

            for j in range(burn_in_period):
                sample, rejections_this_sample = self.next_sample()
                rejections += rejections_this_sample
                # TODO does this number make sense to compare? Maybe average rej/sample?

            sample, rejections_this_sample = self.next_sample()
            rejections += rejections_this_sample

            samples[:, i] = sample

        # end = time.perf_counter()

        # elapsed = end - start

        return samples

    # def next_sample(self):
    #     if self.variant == HRVariant.VANILLA or self.variant == HRVariant.VANILLA_SMT:
    #         return self.next_sample_vanilla()
    #     elif self.variant == HRVariant.SHRINKING or self.variant == HRVariant.SHRINKING_SMT:
    #         return self.next_sample_with_shrinking()
    #     elif self.variant == HRVariant.CDHR:
    #         return self._next_sample_cdhr()
    #     else:
    #         return self.next_sample_z3()

    def _next_sample_vanilla(self):
        # normal random directions hit-and-run (rdhr)
        b = self.current_point

        success = False
        while not success:
            a = self._random_direction()
            inter, success = self._line_box_intersection(a, b, self.bounding_box)

        inter_1 = inter[0]
        inter_2 = inter[1]

        success = False
        rejections = -1

        while not success:
            rnd = np.random.uniform()

            sample = []
            for i in range(len(inter_1)):
                x_0 = inter_1[i]
                x_1 = inter_2[i]
                s_i = (x_1 - x_0) * rnd + x_0
                sample.append(s_i)

            success = self.constraint.evaluate(sample)
            rejections += 1

        self.current_point = sample

        return sample, rejections

    def _next_sample_rdhr_shrinking(self):
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
                s_i = b[i] + rnd * a[i]
                sample.append(s_i)

            success = self.constraint.evaluate(sample)

            if not success:
                if rnd > 0:
                    r_max = rnd
                else:
                    r_min = rnd

            rejections += 1

        # FELIX: fixed bug in next line, 30.03.
        self.current_point = sample

        return sample, rejections

    def _next_sample_cdhr(self):
        b = self.current_point

        success = False
        while not success:
            a, direction_int = self._random_direction_cdhr()
            inter, success = self._line_box_intersection_cdhr(a, direction_int, b, self.bounding_box)

        inter_1 = inter[0]
        inter_2 = inter[1]

        success = False
        rejections = -1

        while not success:
            rnd = np.random.uniform()



            sample = []
            for i in range(len(inter_1)):
                x_0 = inter_1[i]
                x_1 = inter_2[i]
                s_i = (x_1 - x_0) * rnd + x_0
                sample.append(s_i)

            success = self.constraint.evaluate(sample)
            rejections += 1

        self.current_point = sample

        return sample, rejections

    def next_sample_cdhr_shrinking(self):
        # assert (False), 'Not yet implemented.'  # TODO check whether this is even theoretically sound
        b = self.current_point

        success = False
        while not success: # This should only do one iteration?
            a, direction_int = self._random_direction_cdhr()
            inter, success = self._line_box_intersection_cdhr(a, direction_int, b, self.bounding_box)

        inter_1 = inter[0]
        inter_2 = inter[1]

        # on the numer line, minus b[dir_int] describes the translation such that the current point now has value zero
        #  in the axis parallel to the chosen line
        r_min = inter_1[direction_int] - b[direction_int]
        r_max = inter_2[direction_int] - b[direction_int]

        success = False
        rejections = -1


        while not success:
            rnd = np.random.uniform(r_min, r_max)

            # sample = []
            # for i in range(len(inter_1)):
            #     s_i = b[i] + rnd * a[i]
            #     sample.append(s_i)
            sample = b.copy()
            sample[direction_int] += rnd # only one component changes in cdhr and vector is unit vector. simply add

            success = self.constraint.evaluate(sample)

            if not success:
                if rnd > 0:
                    r_max = rnd
                else:
                    r_min = rnd

            rejections += 1

            # FELIX: fixed bug in next line, 30.03.
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
                result = a[i] * ps + b[i]
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
            solution = a * ps + b
            solutions.append(solution)

        if len(solutions) >= 2:
            flag = True
        else:
            flag = False

        return solutions, flag

    def _sort_first(self, l):
        return l[0]

    # def _starting_point(self):
    #     if self.variant == HRVariant.SMT or self.variant == HRVariant.SHRINKING_SMT or self.variant == HRVariant.VANILLA_SMT or self.variant == HRVariant.CDHR:
    #         return self._starting_point_smt()
    #     else:
    #         return self._starting_point_pso()

    def _starting_point_pso(self):

        lb = []
        ub = []
        for b in self.bounding_box:
            lb.append(b[0])
            ub.append(b[1])

        # out, rob_opt = pso(self._evaluate, lb, ub, f_ieqcons=None, swarmsize=10, omega=0.5, phip=0.5,
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
            out_d[str(var)] = num / den

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
        direction = direction / np.linalg.norm(direction)
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
            z, _ = self.next_sample()  # this will set also self.current_point = z
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

        sign = np.random.rand() < 0.5  # random bit
        direction = np.random.randint(low=0, high=n)

        out = np.zeros(n)
        out[direction] = 1

        if sign:
            pass  # plus
        else:
            out[direction] *= -1  # minus

        return out, direction
        # here I return direction, seems like unnecessary extra steps to compute argmax in _next_sample_cdhr


if __name__ == '__main__':
    np.random.seed(2)
    dim = 2
    thickness = 0.1
    var_names = ['x' + str(i) for i in range(dim)]

    # Define the set of constraint TODO this constraint defining is still a little clunky... even for the n-sphere
    c = Constraints(var_names)
    # square_list = ['(' + str(name) + '*' + str(name) + ')' for name in var_names]
    square_list = [str(name) + '*' + str(name) for name in var_names] # operator priority is correct now

    constraint_str = '+'.join(square_list) + '< 1'
    constraint_str2 = '+'.join(square_list) + '> (1-' + str(thickness) + ')' + '* (1-' + str(thickness) + ')'
    c.add_constraint(constraint_str)
    c.add_constraint(constraint_str2)

    # Define the bounding hyperrectangle

    # for name in var_names:
    # locals()[name + '_bound'] =  [-1,1] # not necessary

    bounds = list([[-1, 1] for name in var_names])

    hr = HitAndRun(constraint=c, bounding_box=bounds, direction_sampling=DirectionSampling.CDHR,
                   shrinking=Shrinking.SHRINKING, init_point=InitPoint.SMT)


    import cProfile

    cProfile.run('samples = hr.sampler(100,burn_in_period=200)','restats')
    # print(samples)
    import pstats
    from pstats import SortKey
    p = pstats.Stats('restats')
    # p.strip_dirs().sort_stats(-1).print_stats()

    p.sort_stats(SortKey.TIME).print_stats()

    # from matplotlib import patches
    # circ1 = patches.Circle([0,0], 1, fill=False)
    # circ2 = patches.Circle([0,0], 1-thickness, fill=False)
    #
    # fig, ax = plt.subplots(1,subplot_kw={'adjustable' : 'box', 'aspect' : 'equal'})
    #
    # ax.scatter(samples[0, :], samples[1, :], s = 3)
    # ax.add_patch(circ1)
    # ax.add_patch(circ2)
    # plt.show()




