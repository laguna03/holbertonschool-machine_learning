#!/usr/bin/env python3
"""
Module for add_arrays.
"""


def add_arrays(arr1, arr2):
    """
    Function that adds two arrays element-wise.

    Args:
        arr1 (list): The first array.
        arr2 (list): The second array.

    Returns:
        list: A new array containing the element-wise sums of arr1 and arr2.
              Returns None if the arrays have different lengths.
    """

    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
