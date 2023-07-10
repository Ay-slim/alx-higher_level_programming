#!/usr/bin/python3
"""Module for the is_same_class_funtion"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or its subclass"""
    return isinstance(obj, a_class)
