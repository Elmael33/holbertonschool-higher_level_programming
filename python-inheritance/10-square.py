#!/usr/bin/python3
"""
This module defines the Rectangle class that inherits from BaseGeometry.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square using Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """
        return (self.__size * self.__size)
