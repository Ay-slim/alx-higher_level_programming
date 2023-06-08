#!/usr/bin/python3
import sys


def print_args():
    length = len(sys.argv) - 1
    args = sys.argv
    if (length < 1):
        print("{} arguments.".format(length))
    elif (length == 1):
        print("{} argument:".format(length))
        print("{}: {}".format(length, args[1]))
    else:
        print("{} arguments:".format(length))
        for i in range(1, length + 1):
            print("{}: {}".format(i, args[i]))


if __name__ == "__main__":
    print_args()
