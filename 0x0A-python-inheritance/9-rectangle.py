#!/usr/bin/python3
"""Module for Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class setup"""

    def __init__(self, width, height):
        """Initialization of Rectangle class"""

        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Function to calculate the area of an instance
        of the rectanble class
        """

        return self.__width * self.__height

    def __str__(self):
        """Show a string description of a rectangle instance"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
