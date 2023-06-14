#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for j in list(a_dictionary):
        a_dictionary[j] = 2 * a_dictionary[j]
    return a_dictionary
