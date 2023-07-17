#!/usr/bin/python3
"""Module for Base class initialization"""
import json
import csv


class Base:
    """Setting up a base class with a private class attribute __nb_objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of Base class
        Args:
            id: Id value to be self incremented
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def integer_validator(self, name, value):
        """Validate that input values are integers and greater than 0"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if name in ['height', 'width'] and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if name in ['x', 'y'] and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def to_json_string(list_dictionaries):
        """Return a list of dictionaries as a JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Converts a list of objects to a csv file"""
        f_n = cls.__name__ + ".json"
        with open(f_n, "w") as outfile:
            if list_objs is None:
                outfile.write("[]")
            else:
                dicts_arr = []
                for i in list_objs:
                    dicts_arr.append(i.to_dictionary())
                outfile.write(Base.to_json_string(dicts_arr))

    def from_json_string(json_string):
        """Returns the JSON representation of a string of dicts list"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns a class that was created using a dict of attributes"""
        if dictionary and len(dictionary) > 0:
            if cls.__name__ == "Rectangle":
                obj = cls(1, 1)
            else:
                obj = cls(1)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of classes created
        from a file arg containig JSON strs
        """
        f_n = str(cls.__name__ + ".json")
        try:
            with open(f_n, "r") as outfile:
                dicts_arr = Base.from_json_string(outfile.read())
                return [cls.create(**k) for k in dicts_arr]
        except IOError:
            return []
