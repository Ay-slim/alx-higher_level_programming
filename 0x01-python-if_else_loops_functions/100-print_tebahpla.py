#!/usr/bin/python3
j = 0
for i in range(122, 96, -1):
    k = 0
    if ((j % 2) != 0):
        k = 32
    print("{}".format(chr(i - k)), end="")
    j += 1
