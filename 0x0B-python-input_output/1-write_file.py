#!/usr/bin/python3
"""Write file module"""


def write_file(filename="", text=""):
    """Function to write text to a file and return no of chars
    args:
        filename: Name of file to write to
        text: Text to write to file
    return:
        Length of written text characters
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
