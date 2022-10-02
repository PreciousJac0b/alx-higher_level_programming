#!/usr/bin/python3

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def  test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)
            
    def test_two_args(self):
        r1 = Rectangle(5, 6)
        r2 = Rectangle(4, 5)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(5, 6, 7)
        r2 = Rectangle(4, 5, 6)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(6, 3, 5, 4)
        r2 = Rectangle(5, 4, 5, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)
