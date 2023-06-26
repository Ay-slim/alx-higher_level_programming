#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        li = 0
        k = 0
        for j in my_list:
            k += 1
            if k > x:
                print("{}".format("\n"), end='')
                return li
            if str(j).isdigit():
                li += 1
                print("{:d}".format(int(j)), end='')
            else:
                continue
        print("{}".format("\n"), end='')
        return li
    except IndexError:
        raise IndexError
