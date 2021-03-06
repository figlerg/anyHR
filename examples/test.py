# Import modules
import numpy as np
import time
import matplotlib.pyplot as plt
from anyHR.constraint.Constraint import Constraints
from anyHR.hit_and_run.hit_and_run import HitAndRun


def main_hit_and_run_2D_ball():
    # Define variables to use
    var_names = ['x', 'y']

    # Define the set of constraint
    c = Constraints(var_names)
    c.add_constraint('(x*x) + (y*y) < 1')
    c.add_constraint('(x*x) + (y*y) > 0.9')

    # Define the bounding hyperrectangle
    x_bound = [-10, 10]
    y_bound = [-10, 10]
    bounds = [x_bound, y_bound]

    hr = HitAndRun(S=c, B=bounds)

    a_s = []
    r_s = [[0, 0]]
    total_rejections = 0
    nb_samples = 100
    for i in range(nb_samples * 100):
        sample, rejections = hr._next_sample_cdhr()
        total_rejections = total_rejections + rejections
        a_s.append(sample)
    import random
    a_s = random.sample(a_s, nb_samples)

    print('Total number of rejections: ' + str(total_rejections))

    xs = [sample[0] for sample in a_s]
    ys = [sample[1] for sample in a_s]

    plt.scatter(xs,ys)
    plt.show()
    # plot_samples_2D(0, 1, var_names[0], var_names[1], a_s, r_s, None)

def sample_n_sphere_hr(dim:int, n = 100, burn_in_period = 100, thickness = 0.1):

    start = time.perf_counter()

    var_names = ['x' + str(i) for i in range(dim)]

    # Define the set of constraint
    c = Constraints(var_names)
    square_list = ['(' + str(name) + '*' + str(name) + ')' for name in var_names]

    constraint_str = '+'.join(square_list) + '< 1'

    constraint_str2 = '+'.join(square_list) + '> (1-' + str(thickness) + ')' + '* (1-' + str(thickness) + ')'

    c.add_constraint(constraint_str)
    c.add_constraint(constraint_str2)

    # Define the bounding hyperrectangle

    # for name in var_names:
    # locals()[name + '_bound'] =  [-1,1] # not necessary

    bounds = list([[-1,1] for name in var_names])


    hr = HitAndRun(constraint=c, bounding_box=bounds)

    a_s = []
    r_s = [[0, 0]]


    samples = np.ndarray((dim, n))
    rejections = 0

    for i in range(n):

        for j in range(burn_in_period):
            sample, rejections_this_sample = hr.next_sample()
            rejections += rejections_this_sample # TODO does this number make sense to compare?

        sample, rejections_this_sample = hr.next_sample()
        rejections += rejections_this_sample

        samples[:,i] = sample

    end = time.perf_counter()

    elapsed = end-start

    return rejections, elapsed, samples

def plot_2d_proj(samples, thickness = None):
    circ = plt.Circle((0,0), 1, fill=False)

    fig, ax = plt.subplots(1, subplot_kw={'adjustable' : 'box', 'aspect' : 'equal'})
    ax.scatter(samples[0,:], samples[1,:], s= 3)
    ax.add_patch(circ)

    if thickness:
        circ_inner = plt.Circle((0,0), 1-thickness, fill=False)
        ax.add_patch(circ_inner)

    plt.show()


def min_example():
    # Define variables to use
    var_names = ['x', 'y']

    # Define the set of constraint
    c = Constraints(var_names)
    c.add_constraint('x+y < 1')

    # Define the bounding hyperrectangle
    x_bound = [0, 1]
    y_bound = [0, 1]
    bounds = [x_bound, y_bound]

    # build hr object
    hr = HitAndRun(constraint=c, bounding_box=bounds)

    # generate samples
    samples = []
    total_rejections = 0
    nb_samples = 100
    mixing = 10
    for i in range(nb_samples * mixing):
        sample, rejections = hr.next_sample()

        # do some mixing in between samples
        if i % mixing == 0:
            samples.append(sample)

    xs = [sample[0] for sample in samples]
    ys = [sample[1] for sample in samples]

    plt.scatter(xs,ys)
    plt.show()
    # plot_samples_2D(0, 1, var_names[0], var_names[1], a_s, r_s, None)


if __name__ == '__main__':
    # rejections, elapsed, samples = sample_n_sphere_hr(dim=2)
    # plot_2d_proj(samples, thickness = 0.1)

    min_example()
