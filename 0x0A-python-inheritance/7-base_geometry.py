#!/usr/bin/python3
"""Module for geometry class creation"""


class BaseGeometry:
    """Base Geometry class"""

    def area(self):
        """Throws an exception about non implementation of area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as being an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
