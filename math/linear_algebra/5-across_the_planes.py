#!/usr/bin/env python3
"""
Module for 5-across_the_planes.py
Contains a function that adds two matrices element-wise
"""

def add_matrices2D(mat1, mat2):
    """
    Function that adds two matrices element-wise.

    Args:
        mat1 (list): The first matrix.
        mat2 (list): The second matrix.

    Returns:
        list: A new matrix containing the element-wise sums of mat1 and mat2.
              Returns None if the matrices have different shapes.
    """

    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
