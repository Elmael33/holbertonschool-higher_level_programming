#!/usr/bin/python3
"""
This module is a function appends at the end of UTF-8 encoded
text file and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Appends the end of the text file and return the size
    of the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
