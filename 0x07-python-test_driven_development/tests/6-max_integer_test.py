#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_at_the_end(self):
        """Test for max integer function"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_the_beginning(self):
        """Test for max integer function"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_the_middle(self):
        """Test for max integer function"""
        self.assertEqual(max_integer([1, 4, 3]), 4)

    def test_one_negative_number(self):
        """Test for max integer function"""
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)

    def tests_only_negative_numbers(self):
        """Test for max integer function"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_list_of_one_element(self):
        """Test for max integer function"""
        self.assertEqual(max_integer([4]), 4)

    def test_list_is_empty(self):
        """Test for max integer function"""
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
