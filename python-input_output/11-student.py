#!/usr/bin/python3
"""
This module is provides a class Student that
reading and printing the contents of a file
"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes Student instance with first_name, last_name, and age"""
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        

    def to_json(self, attrs=None):
        """Returns a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    my_dict[key] = self.__dict__[key]
            return my_dict
        
    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance with values from a JSON dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
