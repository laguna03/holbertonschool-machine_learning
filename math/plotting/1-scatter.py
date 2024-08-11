#!/usr/bin/env python3
"""
This module contains a function to plot a scatter graph of men's height vs weight.
"""

import numpy as np
import matplotlib.pyplot as plt


def scatter():
    """
    Plots a scatter graph of men's height vs weight using generated data.
    """

    mean = [69, 0]  # Mean values for height and weight
    cov = [[15, 8], [8, 15]]  # Covariance matrix
    np.random.seed(5)  # Seed for reproducibility
    x, y = np.random.multivariate_normal(mean, cov, 2000).T
    y += 180  # Adjust weight data to realistic values

    plt.figure(figsize=(6.4, 4.8))  # Set the figure size

    plt.scatter(x, y, c='magenta', s=10)  # Scatter plot with magenta points
    plt.title("Men's Height vs Weight")  # Set the title
    plt.xlabel('Height (in)')  # Set the x-axis label
    plt.ylabel('Weight (lbs)')  # Set the y-axis label
    plt.show()  # Display the plot

    return
