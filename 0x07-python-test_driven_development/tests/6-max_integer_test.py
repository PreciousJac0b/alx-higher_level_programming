#!/usr/bin/python3
"""Unittest for the 6-max_integer module"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines several unittests"""
    def test_unordered_list(self):
        """Tests an unordered list"""
        unordered = [3, 2, 4, 5, 6]
        self.assertEqual(max_integer(unordered), 6)

    def test_ordered_list(self):
        """Tests an ordered list"""
        ordered = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(ordered), 5)

    def test_inverted_order(self):
        """Tests a list in reverse ordered manner"""
        reversed_list = [5, 4, 3, 2, 1]
        self.assertEqual(max_integer(reversed_list), 5)

    def test_empty_list(self):
        """Tests an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [3]
        self.assertEqual(max_integer(one_element), 3)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
