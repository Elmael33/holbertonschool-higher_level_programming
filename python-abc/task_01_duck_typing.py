#!/usr/bin/env python3
"""
This module defines an abstract class Shape and
its concrete subclasses Circle and Rectangle.
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """An abstract class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Abstract method to compute the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to compute the perimeter of the shape."""
        pass


class Circle(Shape):
    """A class representing a circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """A class representing a rectangle."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of the given shape."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
