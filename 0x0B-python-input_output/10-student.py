#!/usr/bin/python3
"""Module containing Student class"""


class Student:
    """A template for student instances"""

    def __init__(self, first_name, last_name, age):
        """A function to initialize an instance of the Student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns attributes of a Student class instance present
        in attrs if it is a list of strings. Otherwise, it returns
        all attributes of the instance
        """

        all_string = True
        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    all_string = False

        if type(attrs) is not list or all_string is False:
            return self.__dict__

        self_dict = self.__dict__
        ret_dict = {}

        if len(attrs) > 0:
            for j in attrs:
                if j in self_dict:
                    ret_dict[j] = self_dict[j]
        return ret_dict
