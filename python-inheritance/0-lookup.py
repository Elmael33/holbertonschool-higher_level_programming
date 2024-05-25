#!/usr/bin/python3
"""
This module defines a function called "lookup" that returns a list
of an object's attributes and methods.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    return dir(obj)
