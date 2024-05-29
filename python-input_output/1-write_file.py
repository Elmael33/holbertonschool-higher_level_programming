#!/usr/bin/python3
"""
This module is a function to write a UTF-8 encoded text file
and returns the number of characters
"""


def write_file(filename="", text=""):
    """
    Write the text to the file and return the size of the string
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
