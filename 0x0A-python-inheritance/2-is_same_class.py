#!/usr/bin/python3
"""Module for the is_same_class_funtion"""


def is_same_class(obj, a_class):
    return type(obj).__name__ == a_class.__name__
