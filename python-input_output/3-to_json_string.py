#!/usr/bin/python3
"""
This module is a function that returns
the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """
    Return the representation of a object using JSON
    """
    return json.dumps(my_obj)
