#!/usr/bin/python3
"""Square class with initialization"""


class Square:
    """Square template"""

    def __init__(self, size=0, position=(0, 0)):
        """Define initialization function
        Args:
            size(int): New square size
            position(tuple): Tuple of square coordinates
        """
        self.__size = size
        self.__position = position

    def size(self):
        """Return size private attribrute"""
        return self.__size

    def position(self):
        """Return size private attribute position"""
        return self.__position

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

    def position(self, value):
        """Define position setter function
        Args:
            value(int): New square size
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Define public instance method area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square"""
        size = self.__size
        if size == 0:
            print()
        else:
            for k in range(self.position[1]):
                print()
            for i in range(size):
                for j in range(size):
                    if (j == size - 1):
                        print('#')
                    else:
                        print('#', end='')
