#!/usr/bin/python3
"""Print square module"""


def print_square(size):
    """Print square size"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for j in range(size):
        print("#" * size)
