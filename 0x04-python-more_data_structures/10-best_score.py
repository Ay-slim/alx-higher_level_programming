#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    starter = 0
    for i in list(a_dictionary):
        if a_dictionary[i] is None:
            return None
        if a_dictionary[i] > starter:
            starter = a_dictionary[i]
            max_key = i
    return max_key
