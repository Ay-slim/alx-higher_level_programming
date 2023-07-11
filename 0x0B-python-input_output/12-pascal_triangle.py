#!/usr/bin/python3
"""Module to return pascals triangle"""


def pascal_triangle(n):
    """Function to return pascal's triangle"""

    pas = []
    if n <= 0:
        return pas
    pas.append([1])
    if n == 1:
        return pas
    pas.append([1, 1])
    if n == 2:
        return pas
    for i in range(3, n + 1):
        tmp = [1]
        for j in range(len(pas[-1]) - 1):
            tmp.append(pas[-1][j] + pas[-1][j + 1])
        tmp.append(1)
        pas.append(tmp)
    return pas
