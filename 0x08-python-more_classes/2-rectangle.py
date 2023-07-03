#!/usr/bin/python3
"""Module to define a rectangle class with initialization"""


class Rectangle:
    """A template for square objets"""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle instance
        Args:
            width (int): New square width
            height (int): New square height
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height

    def width(self):
        """Function to return the width of a rectangle"""
        return self.__width

    def height(self):
        """Function to return the height of a rectangle"""
        return self.__height

    def width(self, value):
        """Function to set rectangle width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self, value):
        """Function to set rectangle height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function to return the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Function to return the perimeter of a rectangle"""
        return 2 * (self.__width + self.__height)
