#!/usr/bin/env python3
"""
Module for calculating the shape of a matrix.

This module contains a function `matrix_shape` that takes a matrix as input
and returns a list representing the dimensions (shape) of the matrix. The
shape is determined by the number of elements in each dimension of the matrix.
"""


def matrix_shape(matrix):
    """
    Function that calculates the shape of a matrix.

    Args:
        matrix (list): A list of lists representing the matrix.

    Returns:
        list: A list of integers representing the shape of the matrix.
              The first element represents the number of rows, the second
              the number of columns, and so on.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
