#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list and includes
a method to print the list in sorted order.
"""


class MyList(list):
    """
    A subclass of list with a method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Print the list in ascending order.
        """
        print(sorted(self))
