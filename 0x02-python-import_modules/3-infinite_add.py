#!/usr/bin/python3
import sys


def add_args():
    args = sys.argv
    length = len(args)
    sum = 0
    if length > 1:
        for i in range(1, length):
            sum += int(args[i])
    return sum


if __name__ == "__main__":
    print(add_args())
