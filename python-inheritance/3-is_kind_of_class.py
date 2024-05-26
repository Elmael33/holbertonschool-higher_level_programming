#!/usr/bin/python3
"""
This module defines a function to check if an object
is exactly an instance of a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class

    Return:
    True if object is an exact instance of the specified class,
    False otherwise.
    """
    return isinstance(obj, a_class)
