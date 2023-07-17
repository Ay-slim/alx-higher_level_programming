#!/usr/bin/python3
"""Module for Base class initialization"""


class Base:
    """Setting up a base class with a private class attribute __nb_objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of Base class
        Args:
            id: Id value to be self incremented
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def integer_validator(self, name, value):
        """Validate that input values are integers and greater than 0"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if name in ['height', 'width'] and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if name in ['x', 'y'] and value < 0:
            raise ValueError("{} must be >= 0".format(name))
