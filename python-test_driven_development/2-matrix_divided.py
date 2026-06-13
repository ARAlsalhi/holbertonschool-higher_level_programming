#!/usr/bin/python3
"""This module provides a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div."""
    message = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list or matrix == []:
        raise TypeError(message)

    row_size = None

    for row in matrix:
        if type(row) is not list or row == []:
            raise TypeError(message)

        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        for num in row:
            if type(num) not in [int, float]:
                raise TypeError(message)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
