#!/usr/bin/env python3
"""
This module defines the VerboseList class that extends the built-in list class
and provides notifications for certain list operations.
"""


class VerboseList(list):
    """
    A list subclass that provides notifications
    for append, extend, remove, and pop operations.
    """

    def append(self, item):
        """
        Adds an item to the end of the list and prints a notification.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extends the list by appending elements from
        the iterable and prints a notification.
        """
        items_count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{items_count}] items.")

    def remove(self, item):
        """
        Removes the first occurrence of the item from
        the list and prints a notification.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Removes and returns the item at the specified
        position and prints a notification.
        """
        item = self[index]
        super().pop(index)
        print(f"Popped [{item}] from the list.")
