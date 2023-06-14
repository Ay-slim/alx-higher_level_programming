#!/usr/bin/python3
def uniq_add(my_list=[]):
    summation = 0
    for j in set(my_list):
        summation += j
    return summation
