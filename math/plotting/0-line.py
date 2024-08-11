#!/usr/bin/env python3
"""
This module contains a function to plot a simple line graph using Matplotlib.
The graph plots the cubic values of integers from 0 to 10.
"""

import numpy as np
import matplotlib.pyplot as plt


def line():
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    plt.plot(y, 'r')
    plt.xlim(0, 10)
    plt.show()
    return
