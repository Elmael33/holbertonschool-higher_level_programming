#!/usr/bin/python3
"""
This module defines the Rectangle class that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle using BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
