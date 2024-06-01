#!/usr/bin/python3
"""
This module contains the CustomObject class
"""
import pickle


class CustomObject:
    """
    Custom Object Class.
    """

    def __init__(self, name, age, is_student):
        """
        Constructor method.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """
        Serializes the current instance and saves it to the provided filename.
        """
        try:
            with open(filename, "wb") as myFile:
                pickle.dump(self, myFile)
        except (pickle.PicklingError, FileNotFoundError):
            return None

    def display(self):
        """
        Displays the object's attributes.
        """
        for key, value in self.__dict__.items():
            print("{}: {}".format(key, value))

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an instance from the provided filename.
        """
        try:
            with open(filename, "rb") as myFile:
                return pickle.load(myFile)
        except (
            FileNotFoundError, pickle.UnpicklingError, AttributeError,
            EOFError, ImportError, IndexError
        ):
            return None
