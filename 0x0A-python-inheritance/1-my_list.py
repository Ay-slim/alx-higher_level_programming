#!/usr/bin/python3
"""Module for the MyList class"""


class MyList(list):
    """A class that inherits from the list class"""

    def __init__(self, value=[]):
        """A function to initialize the MyList class"""
        super().__init__(item for item in value)

    def print_sorted(self):
        """Function to print a sorted version of the list"""
        temp = self[:]
        unordered = True
        while (unordered):
            unordered = False
            for i in range(len(temp) - 1):
                if temp[i] > temp[i + 1]:
                    p = temp[i + 1]
                    temp[i + 1] = temp[i]
                    temp[i] = p
                    unordered = True
        print(temp)
