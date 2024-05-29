#!/usr/bin/python3
"""
This module is a function that returns
the JSON representation of an object
"""
import json


def from_json_string(my_str):
    """
    Return the representation of a object using JSON
    """
    return json.loads(my_str)
