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
        self.__size = size

    @property
    def size(self):
        """
        Getting the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setting the size with validation.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character '#'.
        If size is 0, print an empty line.
        """
        if not self.size:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
