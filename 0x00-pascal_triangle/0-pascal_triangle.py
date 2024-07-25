#!/usr/bin/python3
"""
Pascal's Triangle Project
"""


def pascal_triangle(n):
    """
    Pascal's Triangle Project

    This module contains a function that generates Pascal's Triangle
    up to a specified number of levels.

    Functions:
        pascal_triangle(n): Generates Pascal's Triangle up to n levels.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
