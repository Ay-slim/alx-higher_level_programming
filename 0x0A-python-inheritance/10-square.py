#!/usr/bin/python3
"""Module for Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class setup"""

    def __init__(self, size):
        """Initialization of Square class"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Function to calculate square area"""

        return self.__size ** 2
