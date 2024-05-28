#!/usr/bin/python3
"""
This module is a function to read a UTF-8 encoded text file
"""


def read_file(filename=""):
    """
    Prints UTF-8 encoded text file its contents to stdout
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
