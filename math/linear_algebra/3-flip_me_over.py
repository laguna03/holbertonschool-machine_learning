#!/usr/bin/env python3
"""
Module for matrix_transpose.
"""


def matrix_transpose(matrix):
    """
    Function that returns the transpose of a 2D matrix.

    Args:
        matrix (list of lists): The matrix to transpose.

    Returns:
        list of lists: The transposed matrix.
    """
    return [[matrix[j][i] for j in range(len(matrix))]
            for i in range(len(matrix[0]))]
