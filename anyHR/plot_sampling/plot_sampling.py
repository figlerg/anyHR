import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_samples_2D(x: int, y: int, x_name: str, y_name: str, a_samples: list, r_samples: list, hrs: list):
    a_s = [a_samples[x], a_samples[y]]
    r_s = [r_samples[x], r_samples[y]]

    a_s = np.transpose(a_s)
    r_s = np.transpose(r_s)

    fig, ax = plt.subplots(1)

    if a_s.size > 0:
        plt.plot(a_s[0], a_s[1], 'go', markersize=2)
    if r_s.size > 0:
        plt.plot(r_s[0], r_s[1], 'ro', markersize=2)

    x_min = float('inf')
    x_max = -float('inf')
    y_min = float('inf')
    y_max = -float('inf')

    for hr in hrs:
        x_side = hr.sides[0]
        y_side = hr.sides[1]

        x_min = min(x_min, x_side[0])
        x_max = max(x_max, x_side[1])
        y_min = min(y_min, y_side[0])
        y_max = max(y_max, y_side[0])

        rect = patches.Rectangle((x_side[0], y_side[0]), x_side[1] - x_side[0], y_side[1] - y_side[0], linewidth=1,
                                 edgecolor='b', facecolor='none')
        ax.add_patch(rect)

    x_size = x_max - x_min
    y_size = y_max - y_min

    x_min = x_min - 0.05 * x_size
    x_max = x_max + 0.05 * x_size
    y_min = y_min - 0.05 * y_size
    y_max = y_max + 0.05 * y_size

    plt.axis([x_min, x_max, y_min, y_max])

    plt.show()
