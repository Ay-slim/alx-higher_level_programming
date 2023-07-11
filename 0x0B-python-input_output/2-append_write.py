#!/usr/bin/python3
"""Append file module"""


def append_write(filename="", text=""):
    """Function to append text to end of a file and return no of chars
    args:
        filename: Name of file to write to
        text: Text to write to file
    return:
        Length of appended text characters
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
