#!/usr/bin/python3
"""
This module is provides a class Student that
reading and printing the contents of a file
"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes Student instance with first_name, last_name, and age"""
        self.age = age
        self.last_name = last_name
        self.first_name = first_name
        

    def to_json(self, attrs=None):
        """Returns a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
