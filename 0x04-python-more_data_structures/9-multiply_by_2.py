#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for j in list(a_dictionary):
        new_dict[j] = 2 * a_dictionary[j]
    return new_dict
