#!/usr/bin/python3
import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle
import sys
from io import StringIO
"""square class"""


class Test_square(unittest.TestCase):
    """class for testing square"""
    def test_attributes(self):
        """function to test attributes"""
        obj = Square(3, 4, 6)
        self.assertEqual(obj.size, 3)
        self.assertEqual(obj.x, 4)
        self.assertEqual(obj.y, 6)

    def test_area(self):
        """function to test area()"""
        obj = Square(3)
        self.assertEqual(obj.area(), 9)
        obj1 = Square(4)
        self.assertEqual(obj1.area(), 16)

    def test_update(self):
        """function to test update()"""
        obj = Square(3, 4, 6)
        self.assertEqual(obj.size, 3)
        self.assertEqual(obj.x, 4)
        self.assertEqual(obj.y, 6)
        obj.update(1, 2, 3)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 6)
