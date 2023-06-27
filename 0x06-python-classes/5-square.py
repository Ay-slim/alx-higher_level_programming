#!/usr/bin/python3
"""Square class with initialization"""


class Square:
    """Square template"""

    def __init__(self, size=0):
        """Define initialization function
        Args:
            size(int): New square size
        """
        self.__size = size

    def size(self):
        """Return size private attribrute"""
        return (self.__size)

    def size(self, value):
        """Define size setter function
        Args:
            value(int): New square size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Define public instance method area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square"""
        size = self.__size
        if size == 0:
            print()
        else:
            for i in range(size):
                for j in range(size):
                    if (j == size - 1):
                        print('#')
                    else:
                        print('#', end='')
