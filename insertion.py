from matplotlib import pyplot as plt
import numpy as np

# generate sudo-random list of numbers
lst = np.random.randint(0, 100, 20)

# x values for the bar plot
x = range(0, len(lst))


def insertion_sort(lst):
    # loop through the list
    # incrementally check which index to the left should i be placed in
    for i in range(1, len(lst)):

        while lst[i - 1] > lst[i] and i > 0:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i = i - 1

            # plot
            plt.bar(x, lst)
            plt.pause(0.9)
            plt.clf()
    plt.show()
    return lst

print(lst)
print(insertion_sort(lst))