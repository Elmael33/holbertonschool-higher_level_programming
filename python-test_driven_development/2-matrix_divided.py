#!/usr/bin/python3
"""
This module defines a function that divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides each element of a matrix by a divisor and returns the result.

    Args:
        matrix (list): A matrix represented as a list of lists of integers or floats.
        div (int, float): The divisor.

    Returns:
        list: A new matrix with each element divided by the divisor.
    """

    error = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) \
            or not all(isinstance(row, list) for row in matrix) or not matrix:
        raise TypeError(error)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
