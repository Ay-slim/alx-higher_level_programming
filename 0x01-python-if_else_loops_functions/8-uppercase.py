#!/usr/bin/python3
def uppercase(str):
    norm_char = ''
    new_line = '\n'
    for char in str:
        if ord(char) in range(97, 123):
            norm_char = chr(ord(char) - 32)
        else:
            norm_char = char
        print("{}".format(norm_char), end="")
    print("{}".format(new_line), end="")
