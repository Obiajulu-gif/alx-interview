#!/usr/bin/python3
"""
This module contains a function that rotates
a 2D matrix by 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix by 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): a 2D matrix to be rotated.

    Returns:
        None: The matrix is modified in-place
    """

    n = len(matrix)

    for i in range(n):
        for j in range(1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
