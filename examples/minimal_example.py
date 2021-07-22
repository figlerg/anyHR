# Import modules
import numpy as np
import matplotlib.pyplot as plt
from anyHR.constraint.Constraint import Constraints
from anyHR.hit_and_run.hit_and_run import HitAndRun


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