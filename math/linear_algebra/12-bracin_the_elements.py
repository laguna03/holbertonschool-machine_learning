#!/usr/bin/env python3

"""
Module 12-bracin_the_elements
Provides a function np_elementwise to perform element-wise operations on numpy matrices.
"""


def np_elementwise(mat1, mat2):
    """
    Performs element-wise operations on numpy matrices.

    Args:
        mat1 (numpy.ndarray): The first matrix.
        mat2 (numpy.ndarray): The second matrix.

    Returns:
        tuple: A tuple containing the element-wise sum, difference, product, and quotient, respectively.
    """
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
