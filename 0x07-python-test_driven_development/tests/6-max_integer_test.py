#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def regular_list_test(self):
        """Test for max integer function"""
        self.assertEqual(max_integer([2, 4, 6, 8], 8))

    def scrambled_list_test(self):
        """Test for max integer function"""
        self.assertEqual(max_integer([4, 2, 8, 6], 8))
