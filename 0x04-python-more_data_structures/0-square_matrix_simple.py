#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map(lambda x: x**2, each_list)) for each_list in matrix]
