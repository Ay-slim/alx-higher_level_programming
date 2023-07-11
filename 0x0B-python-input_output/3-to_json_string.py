#!/usr/bin/python3
"""Module that converts JSON to string"""


import json


def to_json_string(my_obj):
    """Function that returns the JSON representation of a string
    args:
        my_obj: Object to represent
    return:
        JSON representation of my_obj
    """

    return json.dumps(my_obj)
