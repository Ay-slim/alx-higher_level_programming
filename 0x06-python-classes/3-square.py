#!/usr/bin/python3
"""Square class with initialization"""


class Square:
    """Square template"""

    def __init__(self, size=0):
        """Define initialization function
        Args:
            size(int): New square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Define public instance method area"""
        return self.__size ** 2
