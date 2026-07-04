#!/usr/bin/python3
"""Module that generates Pascal's Triangle."""


def pascal_triangle(n):
    """Return Pascal's Triangle as a list of lists."""
    if n <= 0:
        return []

    triangle = []

    for row_index in range(n):
        row = [1]

        if row_index > 0:
            previous_row = triangle[row_index - 1]

            for column in range(1, row_index):
                value = previous_row[column - 1] + previous_row[column]
                row.append(value)

            row.append(1)

        triangle.append(row)

    return triangle
