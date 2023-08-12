#!/usr/bin/python3
# 6-max_integer_test.py
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_positive_numbers(self):
        """Test a list with positive numbers."""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_positive_negative_numbers(self):
        """Test a list with positive and negative numbers."""
        result = max_integer([-3, 4, -2, 1])
        self.assertEqual(result, 4)

    def test_duplicate_numbers(self):
        """Test a list with duplicate numbers."""
        dupl = [3, 5, 2, 5, 1]
        self.assertEqual(max_integer(dupl), 5)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [5]
        self.assertEqual(max_integer(one_element), 5)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.52, 5.33, -8.423, 5.2, 16.1]
        self.assertEqual(max_integer(floats), 16.1)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.52, 16.5, -9, 1, 16]
        self.assertEqual(max_integer(ints_and_floats), 16.5)

    def test_string(self):
        """Test a string for char with highest num alphabet."""
        string = "Hello"
        self.assertEqual(max_integer(string), 'o')

    def test_list_of_strings(self):
        """Test a list of strings using lexicographic ordering.
        they are compared character by character based on their ASCII values.

        Among these strings, "word" is lexicographically the greatest string
        because it comes after "a", "is" and "Hello" when comparing them
        character by character

        """
        strings = ["Hello", "is", "a", "word"]
        self.assertEqual(max_integer(strings), "word")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
