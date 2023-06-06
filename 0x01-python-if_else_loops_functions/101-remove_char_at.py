#!/usr/bin/python3
def remove_char_at(str, n):
    tmp = [*str]
    length = len(str)
    if (n < 0 or n >= length):
        return str
    tmp.pop(n)
    return ''.join(tmp)
