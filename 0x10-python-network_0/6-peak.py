#!/usr/bin/python3
"""
This module contains the find_peak function
"""


def find_peak(list_of_integers):
    """
    Function to find the peak in a list of unsorted integers
    """
    int_len = len(list_of_integers)
    if not int_len:
        return None
    if int_len == 1:
        return list_of_integers[0]
    for i in range(1, int_len - 1):
        me = list_of_integers[i]
        left = list_of_integers[i - 1]
        right = list_of_integers[i + 1]
        if me >= left and me >= right:
            return me
