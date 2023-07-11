#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """Function to read text from a file and print it
    args:
        filename: Name of file to read from
    return:
        Nothing
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
