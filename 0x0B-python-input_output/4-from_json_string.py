#!/usr/bin/python3
"""Module that parses JSON from string"""


import json


def from_json_string(my_str):
    """Function that returns the string representation of a JSON
    args:
        my_str: String to parse to JSON
    return:
        JSON representation of my_str
    """

    return json.loads(my_str)
