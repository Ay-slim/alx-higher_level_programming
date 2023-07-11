#!/usr/bin/python3
"""Write file module"""


import json


def save_to_json_file(my_obj, filename):
    """Function to save a json to file
    args:
        my_obj: Obj to save to file
        filename: Name of file to write to
    return:
        Nothing
    """

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
