#!/usr/bin/env python3

"""
Module 8-ridin_bareback
Provides a function mat_mul to perform matrix multiplication.
"""


def mat_mul(mat1, mat2):
    """
    Performs matrix multiplication of two 2D lists (matrices).

    Args:
        mat1 (list of list of int/float): The first matrix.
        mat2 (list of list of int/float): The second matrix.

    Returns:
        list of list of int/float or None: The result of the matrix
        multiplication, or None if the matrices cannot be multiplied
        due to incompatible dimensions.
    """
    if len(mat1[0]) != len(mat2):
        return None
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result
