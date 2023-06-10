#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    full_len = len(matrix)
    inner_len = len(matrix[0])
    for i in range(full_len):
        for j in range(inner_len):
            if j == inner_len - 1:
                print("{:d}".format(matrix[i][j]))
                continue
            print("{}".format(matrix[i][j]), end=" ")
