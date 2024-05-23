#!/usr/bin/python3
"""
Module with unittests for the function `max_integer`.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test cases for the 'max_integer' function.
    """

    def test_basic_functioning(self):
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([2, 4, 6, 8]), 8)
        self.assertEqual(max_integer([2, 6, 4]), 6)
        self.assertEqual(max_integer([-2, -4, -6, -8]), -2)

    def test_multiple_maximum_values(self):
        self.assertEqual(max_integer([8, 2, 4, 6, 8, 8]), 8)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_no_arguments(self):
        self.assertEqual(max_integer(), None)

    def test_not_a_list(self):
        with self.assertRaises(TypeError):
            max_integer(2468)

    def test_list_is_not_int(self):
        with self.assertRaises(TypeError):
            max_integer(["2", 4, "6", 8])


if __name__ == '__main__':
    unittest.main()
