#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    max_num = 0
    for i in range(length):
        if max_num >= my_list[i]:
            max_num = max_num
        else:
            max_num = my_list[i]
    return max_num
