#!/usr/bin/env python3
"""
This module contains a function to plot a simple scatter graph using Matplotlib.
The graph plots the cubic values of integers from 0 to 10.
"""

import numpy as np
import matplotlib.pyplot as plt

def scatter():
    """
    Plots a scatter graph of the cubic values of integers from 0 to 10.
    """

    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x, y = np.random.multivariate_normal(mean, cov, 2000).T
    y += 180
    plt.figure(figsize=(6.4, 4.8))

    plt.scatter(x, y, c='magenta', s=10)
    plt.title
    plt.xlabel('Height (in)')
    plt.ylabel('Weight (lbs)')
    plt.title('Men\'s Height vs Weight')
    plt.show()
    return
