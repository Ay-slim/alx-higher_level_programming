#!/usr/bin/python3
"""Module for rectangle class tests"""


from models.base import Base
from models.rectangle import Rectangle
import io
import sys
import unittest


class RectangleClassInitTestCases(unittest.TestCase):
    """A suite of tests to confirm that the __init__ function in the
        rectangle class works as expected
    """

    def test_rectangle_parent_class(self):
        """Affirms that the rectangle class is a child of base class"""
        self.assertIsInstance(Rectangle(3, 8), Base)

    def test_empty_args(self):
        """
        Tests error response when no args are passed for
        width and height
        """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_only_one_arg(self):
        """Tests error response when only one arg is passed"""
        with self.assertRaises(TypeError):
            Rectangle(4)

    def test_min_arg_count(self):
        """
        Test for scenario where minimum no of expected args (two)
        are passed
        """
        ra = Rectangle(10, 2)
        rb = Rectangle(2, 10)
        self.assertEqual(ra.id, rb.id - 1)

    def test_one_optional_arg(self):
        """
        Test for scenario where an optional argument (x) is passed
        """
        ra = Rectangle(3, 1, 8)
        rb = Rectangle(2, 5, 9)
        self.assertEqual(ra.id, rb.id - 1)

    def test_two_optional_args(self):
        """
        Scenario where both optional args (x and y) are passed
        """
        ra = Rectangle(3, 9, 7, 2)
        rb = Rectangle(5, 8, 1, 7)
        self.assertEqual(ra.id, rb.id - 1)

    def test_max_arg_count(self):
        """
        Scenario where the maximum number of arguments is passed
        (width, height, x, y, id)
        """
        self.assertEqual(4, Rectangle(3, 9, 7, 2, 4).id)

    def test_exceed_max_args(self):
        """
        Scenario where the number of arguments exceeds the maximum (5)
        """
        with self.assertRaises(TypeError):
            Rectangle(8, 2, 3, 5, 2, 1)

    def test_width_access(self):
        """
        Test to ensure the private width attribute is not publicly accessible
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4).__width)

    def test_height_access(self):
        """
        Test to ensure the private height attribute is not publicly accessible
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4).__height)

    def test_x_access(self):
        """
        Test to ensure the private x attribute is not publicly accessible
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4).__x)

    def test_y_private(self):
        """
        Test to ensure the private y attribute is not publicly accessible
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4).__y)

    def test_getter_method_width(self):
        """
        Test to ensure the width getter method works
        """
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(1, r.width)

    def test_setter_method_width(self):
        """
        Test to ensure the width setter method works
        """
        r = Rectangle(1, 2, 3, 4)
        r.width = 8
        self.assertEqual(8, r.width)

    def test_getter_method_height(self):
        """
        Test to ensure the height getter method works
        """
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(2, r.height)

    def test_setter_method_height(self):
        """
        Test to ensure the height setter method works
        """
        r = Rectangle(1, 2, 3, 4)
        r.height = 7
        self.assertEqual(7, r.height)

    def test_getter_method_x(self):
        """
        Test to ensure the x getter method works
        """
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(3, r.x)

    def test_setter_method_x(self):
        """
        Test to ensure the x setter method works
        """
        r = Rectangle(1, 2, 3, 4)
        r.x = 8
        self.assertEqual(8, r.x)

    def test_getter_method_y(self):
        """
        Test to ensure the y getter method works
        """
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(4, r.y)

    def test_setter_method_y(self):
        """
        Test to ensure the y setter method works
        """
        r = Rectangle(1, 2, 3, 4)
        r.y = 8
        self.assertEqual(8, r.y)


class RectangleClassWidthTestCases(unittest.TestCase):
    """A suite of tests for the width rectangle class attribute"""

    def test_None_arg(self):
        """Scenario where None is passed as the width arg"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 1)

    def test_str_arg(self):
        """Scenario where a string is passed as the width arg"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("string", 1)

    def test_float_arg(self):
        """Scenario where a float is passed as the width arg"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.2, 1)

    def test_complex_arg(self):
        """Scenario where a complex number is passed as the width arg"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(1), 1)

    def test_dict_arg(self):
        """Scenario where a dict is passed as the width arg"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"first": 1, "second": 2}, 1)

    def test_bool_arg(self):
        """Scenario where a boolean is passed as the width arg"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 1)

    def test_list_arg(self):
        """Scenario where a list is passed as the width arg"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(['a', 'b', 'c'], 1)

    def test_tuple_arg(self):
        """Scenario where a tuple is passed as the width arg"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 1)

    def test_range_arg(self):
        """Scenario where a range is passed as the width arg"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(12), 1)

    def test_nan_arg(self):
        """Scenario where NaN is passed as the width arg"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 1)

    def test_negative_arg(self):
        """Scenario where a negative value is passed as the width arg"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 1)

    def test_zero_arg(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1)

class RectangleClassHeightTestCases(unittest.TestCase):
    """A suite of tests for the height rectangle class attribute"""

    def test_None_argheight(self):
        """Scenario where None is passed as the height arg"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None))

    def test_str_argheight(self):
        """Scenario where a string is passed as the height arg"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "string")

    def test_float_argheight(self):
        """Scenario where a float is passed as the height arg"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 1.2)

    def test_complex_argheight(self):
        """Scenario where a complex number is passed as the height arg"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(1))

    def test_dict_argheight(self):
        """Scenario where a dict is passed as the height arg"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"first": 1, "second": 2})

    def test_bool_argheight(self):
        """Scenario where a boolean is passed as the height arg"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, False)

    def test_list_argheight(self):
        """Scenario where a list is passed as the height arg"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, ['a', 'b', 'c'])

    def test_tuple_argheight(self):
        """Scenario where a tuple is passed as the height arg"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))

    def test_range_argheight(self):
        """Scenario where a range is passed as the height arg"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(12))

    def test_nan_argheight(self):
        """Scenario where NaN is passed as the height arg"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'))

    def test_negative_argheight(self):
        """Scenario where a negative value is passed as the height arg"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -3)

    def test_zero_argheight(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


if __name__ == "__main__":
    unittest.main()
