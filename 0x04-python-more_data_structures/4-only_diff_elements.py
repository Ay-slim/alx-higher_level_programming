#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    comm_1 = {i for i in set_1 if i not in set_2}
    comm_2 = {j for j in set_2 if j not in set_1}
    return comm_1.union(comm_2)
