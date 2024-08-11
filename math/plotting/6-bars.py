#!/usr/bin/env python3
"""Function that plots a stacked bar graph."""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """Plot a stacked bar graph representing the number of fruit each person possesses."""
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))

    names = ['Farrah', 'Fred', 'Felicia']
    colors = ['r', 'yellow', '#ff8000', '#ffe5b4']  # Colors for apples, bananas, oranges, peaches
    width = 0.5

    # Stacking the bars
    bottom = np.zeros(3)
    for i in range(len(fruit)):
        plt.bar(names, fruit[i], width, color=colors[i], bottom=bottom)
        bottom += fruit[i]

    # Setting labels, title, and legend
    plt.ylabel('Quantity of Fruit')
    plt.title('Number of Fruit per Person')
    plt.legend(['apples', 'bananas', 'oranges', 'peaches'])

    # Setting the y-axis range and ticks
    plt.ylim(0, 80)
    plt.yticks(np.arange(0, 81, 10))

    plt.show()
