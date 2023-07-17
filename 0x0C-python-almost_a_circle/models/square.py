#!/usr/bin/python3
"""Module containing the square class definition, attributes and methods"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class definition, methods, and attributes"""

    def __init__(self, size, x=0, y=0, id=None):
        """Function to initialize a Square class instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overload the __str__function inherited from Rectangle class"""
        i = self.id
        x = self.x
        y = self.y
        w = self.width
        return "[Square] ({}) {}/{} - {}".format(i, x, y, w)

    def size(self):
        """Getter method that returns the size of a square"""
        return self.width

    def size(self, value):
        """Setter method for setting the size of a square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates attributes with arg values"""
        args_len = len(args)
        attrs = ['id', 'size', 'x', 'y']
        if args and args_len > 0:
            for i in range(args_len):
                if i == 0:
                    if attrs[i] is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = args[i]
                else:
                    setattr(self, attrs[i], args[i])
        elif kwargs and len(kwargs) > 0:
            for key, val in kwargs.items():
                if key == 'id':
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val
                else:
                    setattr(self, key, val)

    def to_dictionary(self):
        """Function to return a square object instance as dict"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
