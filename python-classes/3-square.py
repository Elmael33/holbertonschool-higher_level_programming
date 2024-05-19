#!/usr/bin/python3
"""
This module defines an empty class named Square.
"""


class Square:
    """
    This is an empty class that represents a square.
    """

    def __init__(self, size=0):
        """
        Initialize the Square instance with an optional size as args.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.
        """
        return self.__size ** 2
