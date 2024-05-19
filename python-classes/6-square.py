#!/usr/bin/python3
"""
This module defines an empty class named Square."""


class Square:
    """
    This is an empty class that represents a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the Square instance with an optional size as args.
        """
        self.size = size
        self.position = position

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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getting the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setting the position with validation.
        """
        if not isinstance(value, tuple) or len(value) != 2 \
           or not all(isinstance(x, int) for x in value) \
           or not all(x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        if not self.__size:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
