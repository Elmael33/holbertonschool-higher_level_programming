#!/usr/bin/python3
"""
This module is a function that writes an Object
to a text file, using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file representation
    of a object using JSON
    """
    with open(filename, "w", encoding="utf-8") as file:
        return json.dumps(my_obj)
