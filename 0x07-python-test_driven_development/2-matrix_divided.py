#!/usr/bin/python3
"""Module for matrix divided function"""

def matrix_divided(matrix, div):
    """Matrix division"""
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    row_len_err = "Each row of the matrix must have the same size"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(matrix_error)
    row_length = 0
    for j in range(len(matrix)):
        if not isinstance(matrix[j], list):
            raise TypeError(matrix_error)
        if j == 0:
            row_length = len(matrix[j])
        if len(matrix[j]) != row_length:
            raise TypeError(row_len_err)
        for el in matrix[j]:
            if not isinstance(el, (int, float)):
                raise TypeError(matrix_error)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda k: round(k / div, 2), p)) for p in matrix]
