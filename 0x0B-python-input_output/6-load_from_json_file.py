#!/usr/bin/python3
"""Object from JSON file module"""


import json


def load_from_json_file(filename):
    """Function to load json from a file
    args:
        filename: Name of file to read from
    return:
        Nothing
    """

    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
