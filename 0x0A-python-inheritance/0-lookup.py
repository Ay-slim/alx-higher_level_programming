#!/usr/bin/python3
"""Module for the lookup function"""


def lookup(obj):
    """lookup
    - A function that returns a list containing the
        methods and attributes of an object passed
        to it
    """
    return dir(obj)
