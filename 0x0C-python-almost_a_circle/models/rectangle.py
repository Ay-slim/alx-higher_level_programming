#!/usr/bin/python3
"""Module containing the Rectangle class"""


import sys
from models.base import Base


class Rectangle(Base):
    """Rectangle class from which instances are initialized"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle instance initialization
        attributes:
            width
            height
            x
            y
            id
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        if x != 0 or y != 0:
            self.integer_validator('x', x)
            self.integer_validator('y', y)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter method to get width private variable"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to set width private attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to get height private variable"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to set height private attribute"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method to get x private variable"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method to set x private attribute"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method to get y private variable"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method to set y private attribute"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Public method that returns the area of a rectangle class instance"""
        return self.width * self.height

    def display(self):
        """Public method to draw out the rectangle using the character #"""
        if not self.width > 0 or not self.height > 0:
            print("")
            return

        for j in range(self.y):
            print("")
        for i in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            print('#' * self.width, end="")
            print("")

    def __str__(self):
        """Overriding the __str__ method to control the output when printing"""
        id_val = self.id
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(id_val, x, y, w, h)

    def update(self, *args, **kwargs):
        """Updates attributes with arg values"""

        args_len = len(args)
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args and args_len > 0:
            for i in range(args_len):
                if i == 0:
                    if attrs[i] is None:
                        w = self.width
                        h = self.height
                        x = self.x
                        y = self.y
                        self.__init__(w, h, x, y)
                    else:
                        self.id = attrs[i]
                else:
                    setattr(self, attrs[i], args[i])
        elif kwargs and len(kwargs) > 0:
            for key, val in kwargs.items():
                if key == 'id':
                    if val is None:
                        w = self.width
                        h = self.height
                        x = self.x
                        y = self.y
                        self.__init__(w, h, x, y)
                    else:
                        self.id = val
                else:
                    setattr(self, key, val)

    def to_dictionary(self):
        """Function to return a rectangle object instance as dict"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
