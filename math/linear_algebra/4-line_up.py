#!/usr/bin/env python3
"""
Module for add_arrays.
"""

def add_arrays(arr1, arr2):
    """
    Function that adds two arrays elemment-wise.
    """

    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
