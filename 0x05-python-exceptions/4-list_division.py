#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = len(my_list_1)
    j = len(my_list_2)
    result_list = [0] * list_length
    if (i > j):
        larger = i
        smaller = j
    else:
        larger = j
        smaller = i
    try:
        for k in range(list_length):
            if k == smaller and (i < list_length or j < list_length):
                print('out of range')
                return result_list
            elif not str(my_list_1[k]).isdigit():
                print('wrong type')
            elif not str(my_list_2[k]).isdigit():
                print('wrong type')
            elif my_list_2[k] == 0:
                print('division by 0')
            elif k == smaller and (i < list_length or j < list_length):
                print('out of range')
                return result_list
            else:
                result_list[k] = int(my_list_1[k]) / int(my_list_2[k])
        return result_list
    except ZeroDivisionError:
        pass
    finally:
        pass
