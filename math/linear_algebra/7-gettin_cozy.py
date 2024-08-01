#!/usr/bin/env python3
"""
Module for 7-gettin_cozy.py.
Contains a function that concatenates two matrices along a specific axis.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Function that concatenates two matrices along a specific axis.

    Args:
        mat1 (list): The first matrix.
        mat2 (list): The second matrix.
        axis (int): The axis along which to concatenate the matrices.

    Returns:
        list: A new matrix containing the concatenation of mat1 and mat2 along
              the specified axis. Returns None if the matrices cannot be
              concatenated.
    """

    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row.copy() for row in mat1] + [row.copy() for row in mat2]
    if axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [mat1[i] + mat2[i] for i in range(len(mat1))]
    return None
