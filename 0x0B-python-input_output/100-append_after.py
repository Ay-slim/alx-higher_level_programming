#!/usr/bin/python3
"""Append after module"""


def append_after(filename="", search_string="", new_string=""):
    """Function to append
    args:
        filename: Name of file to check
        search_string: Text to scan for
        new_string: Text to insert
    return:
        Nothing
    """

    ins_str = ""
    i = 0
    with open(filename, 'r', encoding="utf-8") as f:
        while 1 == 1:
            each_line = f.readline()
            if each_line == "":
                break
            if i == 0:
                ins_str += each_line
            else:
                ins_str += each_line
            if search_string in each_line:
                ins_str += new_string
            i += 1

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(ins_str)
