#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        elem_1 = tuple_a[0]
        elem_2 = tuple_a[1]
    if len(tuple_b) >= 2:
        elem_3 = tuple_b[0]
        elem_4 = tuple_b[1]
    if len(tuple_a) == 1:
        elem_1 = tuple_a[0]
        elem_2 = 0
    if len(tuple_b) == 1:
        elem_3 = tuple_b[0]
        elem_4 = 0
    if len(tuple_a) == 0:
        elem_1 = 0
        elem_2 = 0
    if len(tuple_b) == 0:
        elem_3 = 0
        elem_4 = 0
    return (elem_1 + elem_3, elem_2 + elem_4)
