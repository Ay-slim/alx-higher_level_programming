#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for j in list(a_dictionary):
        if a_dictionary[j] == value:
            del a_dictionary[j]
    return a_dictionary
