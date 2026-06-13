#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_ordered_list(self):
        """Test max at the end."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test max at the beginning."""
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_at_middle(self):
        """Test max in the middle."""
        self.assertEqual(max_integer([1, 2, 9, 3]), 9)

    def test_empty_list(self):
        """Test empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test list with one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test list with only negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_mixed_numbers(self):
        """Test list with positive and negative numbers."""
        self.assertEqual(max_integer([-10, 0, 4, -2]), 4)

    def test_duplicate_max(self):
        """Test list with duplicated maximum value."""
        self.assertEqual(max_integer([1, 4, 4, 2]), 4)

    def test_float_numbers(self):
        """Test list with float numbers."""
        self.assertEqual(max_integer([1.5, 3.2, 2.8]), 3.2)


if __name__ == "__main__":
    unittest.main()
