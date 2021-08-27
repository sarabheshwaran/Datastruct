from matplotlib import colors
import matplotlib.pyplot as plt
from random import choice
from Random_walk import RandomWalk
# Make a random walk, and plot the points.


while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='red', s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break