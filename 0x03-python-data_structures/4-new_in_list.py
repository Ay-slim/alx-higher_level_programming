#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    length = len(my_list)
    if idx >= length:
        return my_list
    new_list = []
    for i in range(length):
        if idx == i:
            new_list.append(element)
            continue
        new_list.append(my_list[i])
    return new_list
