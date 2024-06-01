#!/usr/bin/python3
"""
This module provides basic serialization and deserialization functionalities.
"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a dictionary and saves it to a specified JSON file"""
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Loads data from a JSON file and deserializes it to a dictionary"""
    with open(filename, 'r') as file:
        return json.load(file)
