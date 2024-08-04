#!/usr/bin/env python3

"""
Module 13-cats_got_your_tongue
Provides a function np_cat to concatenate numpy matrices.
"""

import numpy as np

def np_cat(mat1, mat2, axis=0):
    """
    Concatenates numpy matrices along a specified axis.

    Args:
        mat1 (numpy.ndarray): The first matrix.
        mat2 (numpy.ndarray): The second matrix.
        axis (int): The axis along which to concatenate the matrices.

    Returns:
        numpy.ndarray: The concatenated matrix.
    """
    return np.concatenate((mat1, mat2), axis=axis)
