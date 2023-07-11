#!/usr/bin/python3
"""class to json module"""


def class_to_json(obj):
    """Class to json function
    args:
        obj: Object whose definition to serialize
    """

    return obj.__dict__
