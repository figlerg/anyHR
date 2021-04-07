import random
import math
import numpy as np
import matplotlib.pyplot as plt


def main():

    for i in range(100):
        a = random.uniform(3.14/2 - 0.2, 3.14/2 + 0.2)
        #a = 3.14/2
        b = 0
        d = random.uniform(9.5, 10.5)

        a1 = a
        b1 = b
        d1 = d

        a2 = -a1
        b2 = a1*d1 + b1
        d2 = d1

        plt.plot([0, d1, d1+d2], [0, b2, a2*d2+b2])

        #x = np.linspace(d1, d1+d2, 100)
        #y = np.exp(a2*x) + b2

        #plt.plot_sampling(x, y)

    plt.show()

if __name__ == "__main__":
    # execute only if run as a script
    main()