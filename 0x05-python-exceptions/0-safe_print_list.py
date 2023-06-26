#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        k = 0
        for j in my_list:
            k += 1
            if k > x:
                print("{}".format("\n"), end='')
                return k - 1
            print("{}".format(j), end='')
        print("{}".format("\n"), end='')
        return k
    except IndexError:
        print("{}".format("x is out of range"))
