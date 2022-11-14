# anyHR
A collection of *hit-and-run Markov Chain Monte Carlo* algorithms for sampling of n-dimensional sets defined by arbitrary inequality constraints.


## Introduction
This tool implements some variants of the *hit and run* or *mixing* algorithms. 

Let **S** be an open bounded set in n dimensions defined by inequality constraints of the form 
f(x<sub>1</sub>,..., x<sub>n</sub>) < g(x<sub>1</sub>,..., x<sub>n</sub>), where f and g are arbitrary functions.
Let all parameters also have parameter ranges defined as intervals, so **S** is a subset of a hyperrectangle.

(As an example, one could impose ``x + y < 1`` in the two dimensional plane, with x in (0,1) and y in (0,1)).

Hit-and-run algorithms can be used to get a sample uniformly at random inside of this set **S**.

**anyHR** parses the parameters and their respective constraints and returns a number of samples that satisfy this spec, 
while being distributed uniformly on the set of allowed values. 
For more information on mixing algorithms see references below.

## Installation
It is necessary to have a working installation of Python 3,
[pip](https://pip.pypa.io/en/stable/installing/) and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)  for the following installation process.
Open the target installation directory in a terminal and type
```bash
pip install anyHR
```

## Use
A minimal running example for the above specification can be sampled with the following code:

````python
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
````

## References
For more information about mixing algorithms, see:

- Smith, R. L. (1984). Efficient Monte Carlo procedures for generating points uniformly distributed over bounded regions. Operations Research, 32(6), 1296-1308.

- Kiatsupaibul, S., Smith, R. L., & Zabinsky, Z. B. (2011). An analysis of a variation of hit-and-run for uniform sampling from general regions. ACM Transactions on Modeling and Computer Simulation (TOMACS), 21(3), 1-11.

- Neal, R. M. (2003). Slice sampling. The annals of statistics, 31(3), 705-767.


We also thank Abraham Lee for his implementation of the PSO algorithms which is used here.
See https://github.com/tisimst/pyswarm for more information.
