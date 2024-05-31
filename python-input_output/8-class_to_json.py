#!/usr/bin/python3
"""
This module converts an object to a JSON-serializable dictionary.
"""


def class_to_json(obj):
    """
    Converts an object to a JSON-serializable dictionary.
    """
    return obj.__dict__
