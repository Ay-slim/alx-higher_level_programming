#!/usr/bin/python3
"""Module to test the Base class implementation"""


import unittest
from models.base import Base


class BaseClassTestCase(unittest.TestCase):
    """A class to test the Base class intialization and methods"""

    def test_empty_decl(self):
        """Test a declaration with no arguments"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_zero_arg(self):
        """Test a declaration with int 0"""
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    def test_negative_arg(self):
        """Test a declaration with negative int"""
        b1 = Base(-5)
        self.assertEqual(b1.id, -5)

    def test_positive_arg(self):
        """Test a declaration with positive int"""
        b4 = Base(4)
        self.assertEqual(b4.id, 4)

    def test_string_arg(self):
        """Test a declaration with string as arg"""
        b1 = Base('whatever')
        self.assertEqual('whatever', b1.id)

    def test_nb_objects_private(self):
        """Confirm that nb objects is a private class attribute"""
        with self.assertRaises(AttributeError):
            self.assertEqual(Base.__nb_objects)

if __name__ == '__main__':
    unittest.main()
