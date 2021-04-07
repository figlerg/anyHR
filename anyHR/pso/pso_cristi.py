####################################################################################################################
# Adaptation of the original PSO implementation from https://github.com/tisimst/pyswarm/blob/master/pyswarm/pso.py #
# in the following ways:                                                                                           #
# - new parameter 'psobudget' (integer) to specify the maximum number of particle updates allowed across the       #
#   iterations; if set to psobudget=swarmsize*maxiter then it has no effect w.r.t. the original method             #
# - new parameter 'threshold' (float); if the objective function evaluates to a value which is below the threshold #
#   (equality excluded) then the optimization search stops; if set to threshold=-np.inf then it has no effect      #
#   w.r.t. the original method                                                                                     #
####################################################################################################################

from functools import partial
import numpy as np


def _obj_wrapper(func, args, kwargs, x):
    return func(x, *args, **kwargs)


def _is_feasible_wrapper(func, x):
    return np.all(func(x) >= 0)


def _cons_none_wrapper(x):
    return np.array([0])


def _cons_ieqcons_wrapper(ieqcons, args, kwargs, x):
    return np.array([y(x, *args, **kwargs) for y in ieqcons])


def _cons_f_ieqcons_wrapper(f_ieqcons, args, kwargs, x):
    return np.array(f_ieqcons(x, *args, **kwargs))


def pso(func, lb, ub, ieqcons=[], f_ieqcons=None, threshold=-np.inf, args=(), kwargs={},
        swarmsize=100, omega=0.5, phip=0.5, phig=0.5, maxiter=100,
        minstep=1e-8, minfunc=1e-8, psobudget=None, debug=False, processes=1,
        particle_output=False):
    """
    Perform a particle swarm optimization (PSO)

    Parameters
    ==========
    func : function
        The function to be minimized
    lb : array
        The lower bounds of the design variable(s)
    ub : array
        The upper bounds of the design variable(s)

    Optional
    ========
    ieqcons : list
        A list of functions of length n such that ieqcons[j](x,*args) >= 0.0 in 
        a successfully optimized problem (Default: [])
    f_ieqcons : function
        Returns a 1-D array in which each element must be greater or equal 
        to 0.0 in a successfully optimized problem. If f_ieqcons is specified, 
        ieqcons is ignored (Default: None)
    threshold : scalar
        The algorithm will try to minimize the objective function to a value
        which is less than the value specified in 'threshold'
        (Default: -np.inf)
        NOTE: this is part of the adaptation
    args : tuple
        Additional arguments passed to objective and constraint functions
        (Default: empty tuple)
    kwargs : dict
        Additional keyword arguments passed to objective and constraint 
        functions (Default: empty dict)
    swarmsize : int
        The number of particles in the swarm (Default: 100)
    omega : scalar
        Particle velocity scaling factor (Default: 0.5)
    phip : scalar
        Scaling factor to search away from the particle's best known position
        (Default: 0.5)
    phig : scalar
        Scaling factor to search away from the swarm's best known position
        (Default: 0.5)
    maxiter : int
        The maximum number of iterations for the swarm to search (Default: 100)
    minstep : scalar
        The minimum stepsize of swarm's best position before the search
        terminates (Default: 1e-8)
    minfunc : scalar
        The minimum change of swarm's best objective value before the search
        terminates (Default: 1e-8)
    psobudget : int
        The maximum number of particle updates allowed across the iterations
        (Default: None, case in which is initialized to maxiter*swarmsize)
        NOTE: this is part of the adaptation
    debug : boolean
        If True, progress statements will be displayed every iteration
        (Default: False)
    processes : int
        The number of processes to use to evaluate objective function and 
        constraints (default: 1)
    particle_output : boolean
        Whether to include the best per-particle position and the objective
        values at those.

    Returns
    =======
    g : array
        The swarm's best known position (optimal design)
    f : scalar
        The objective value at ``g``
    psobudget: scalar
        The remaining budget
        NOTE: this is part of the adaptation
    p : array
        The best known position per particle
    pf: arrray
        The objective values at each position in p

    """

    assert len(lb) == len(ub), 'Lower- and upper-bounds must be the same length'
    assert hasattr(func, '__call__'), 'Invalid function handle'
    lb = np.array(lb)
    ub = np.array(ub)
    assert np.all(ub > lb), 'All upper-bound values must be greater than lower-bound values'

    ignore_budget = False
    if psobudget is None:
        psobudget = maxiter * swarmsize
        ignore_budget = True

    vhigh = np.abs(ub - lb)
    vlow = -vhigh

    # Initialize objective function
    obj = partial(_obj_wrapper, func, args, kwargs)

    # Check for constraint function(s) #########################################
    if f_ieqcons is None:
        if not len(ieqcons):
            if debug:
                print('No constraints given.')
            cons = _cons_none_wrapper
        else:
            if debug:
                print('Converting ieqcons to a single constraint function')
            cons = partial(_cons_ieqcons_wrapper, ieqcons, args, kwargs)
    else:
        if debug:
            print('Single constraint function given in f_ieqcons')
        cons = partial(_cons_f_ieqcons_wrapper, f_ieqcons, args, kwargs)
    is_feasible = partial(_is_feasible_wrapper, cons)

    # Initialize the multiprocessing module if necessary
    if processes > 1:
        import multiprocessing
        mp_pool = multiprocessing.Pool(processes)

    # Initialize the particle swarm ############################################
    S = swarmsize if swarmsize < psobudget else psobudget
    D = len(lb)  # the number of dimensions each particle has
    x = np.random.rand(S, D)  # particle positions
    v = np.zeros_like(x)  # particle velocities
    p = np.zeros_like(x)  # best particle positions
    fx = np.zeros(S)  # current particle function values
    fs = np.zeros(S, dtype=bool)  # feasibility of each particle
    fp = np.ones(S) * np.inf  # best particle function values
    g = []  # best swarm position
    fg = np.inf  # best swarm position starting value

    # Initialize the particle's position
    x = lb + x * (ub - lb)

    # Initialize the particle's velocity
    v = vlow + np.random.rand(S, D) * (vhigh - vlow)

    # Calculate objective and constraints for each particle
    if processes > 1:
        fx = np.array(mp_pool.map(obj, x))
        fs = np.array(mp_pool.map(is_feasible, x))
    else:
        for i in range(S):
            fx[i] = obj(x[i, :])
            fs[i] = is_feasible(x[i, :])
    # update the psobudget and the number of particles S that the new budget allows
    # to be processed at the next iteration
    psobudget -= S
    S = S if S < psobudget else psobudget

    # Store particle's best position (if constraints are satisfied)
    i_update = np.logical_and((fx < fp), fs)
    p[i_update, :] = x[i_update, :].copy()
    fp[i_update] = fx[i_update]

    # Update swarm's best position
    i_min = np.argmin(fp)
    if fp[i_min] < fg:
        fg = fp[i_min]
        g = p[i_min, :].copy()
        if fg < threshold:
            print('Stopping search: global best objective function value below threshold ({}) during initialization' \
                  .format(threshold))
            if particle_output:
                return g, fg, psobudget, p, fp
            else:
                return g, fg, psobudget
        if psobudget == 0:
            print('Stopping search: budget consumed already in the initialization step')
            if particle_output:
                return g, fg, psobudget, p, fp
            else:
                return g, fg, psobudget
    else:
        # There is no feasible starting point!
        if psobudget == 0:
            print('Stopping search: budget consumed already in the initialization step.')
            print("The optimization couldn't find a feasible design. Sorry, try increasing the budget")
            return
        # At the start, there may not be any feasible starting point, so just
        # give it a temporary "best" point since it's likely to change
        g = x[0, :].copy()

    # Iterate until termination criterion met ##################################
    it = 1
    while it <= maxiter:
        rp = np.random.uniform(size=(S, D))
        rg = np.random.uniform(size=(S, D))

        # Update the particles velocities
        v[:S, :] = omega * v[:S, :] + phip * rp * (p[:S, :] - x[:S, :]) + phig * rg * (g - x[:S, :])
        # Update the particles' positions
        x[:S, :] = x[:S, :] + v[:S, :]
        # Correct for bound violations
        maskl = x[:S, :] < lb
        masku = x[:S, :] > ub
        x[:S, :] = x[:S, :] * (~np.logical_or(maskl, masku)) + lb * maskl + ub * masku

        # Update objectives and constraints
        if processes > 1:
            fx[:S] = np.array(mp_pool.map(obj, x[:S, :]))
            fs[:S] = np.array(mp_pool.map(is_feasible, x[:S, :]))
        else:
            for i in range(S):
                fx[i] = obj(x[i, :])
                fs[i] = is_feasible(x[i, :])
        # update the psobudget and the number of particles S that the new budget allows
        # to be processed at the next iteration
        psobudget -= S
        S = S if S < psobudget else psobudget

        # Store particle's best position (if constraints are satisfied)
        i_update = np.logical_and((fx < fp), fs)
        p[i_update, :] = x[i_update, :].copy()
        fp[i_update] = fx[i_update]

        # Compare swarm's best position with global best position
        i_min = np.argmin(fp)
        if fp[i_min] < fg:
            if debug:
                print('New best for swarm at iteration {:}: {:} {:}' \
                      .format(it, p[i_min, :], fp[i_min]))

            p_min = p[i_min, :].copy()
            stepsize = np.sqrt(np.sum((g - p_min) ** 2))

            if np.abs(fg - fp[i_min]) <= minfunc:
                print('Stopping search: Swarm best objective change less than {:}' \
                      .format(minfunc))
                if particle_output:
                    return p_min, fp[i_min], psobudget, p, fp
                else:
                    return p_min, fp[i_min], psobudget
            elif stepsize <= minstep:
                print('Stopping search: Swarm best position change less than {:}' \
                      .format(minstep))
                if particle_output:
                    return p_min, fp[i_min], psobudget, p, fp
                else:
                    return p_min, fp[i_min], psobudget
            else:
                g = p_min.copy()
                fg = fp[i_min]

        if debug:
            print('Best after iteration {:}: {:} {:}'.format(it, g, fg))

        if fg < threshold:
            print('Stopping search: global best objective function value below threshold ({})' \
                  .format(threshold))
            if particle_output:
                return g, fg, psobudget, p, fp
            else:
                return g, fg, psobudget

        if (psobudget == 0) and not ignore_budget:
            print('Stopping search: budget consumed')
            if particle_output:
                return g, fg, psobudget, p, fp
            else:
                return g, fg, psobudget

        it += 1

    print('Stopping search: maximum iterations reached --> {:}'.format(maxiter))

    if not is_feasible(g):
        print("However, the optimization couldn't find a feasible design. Sorry")
    if particle_output:
        return g, fg, psobudget, p, fp
    else:
        return g, fg, psobudget