#!/usr/bin/env python3
"""
This module defines an abstract class Animal and its subclasses Dog and Cat.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    An abstract base class representing an animal.
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    A class representing a dog, a type of animal.
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    A class representing a cat, a type of animal.
    """
    def sound(self):
        return "Meow"
