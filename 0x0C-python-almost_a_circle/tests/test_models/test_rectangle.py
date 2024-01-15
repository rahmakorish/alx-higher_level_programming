#!/usr/bin/python3
import pep8
import unittest
from models.rectangle import Rectangle
from models.base import Base
import sys
from io import StringIO
""" class Base"""


class testingRectangle(unittest.TestCase):
    """class for testing Rectangle"""
    def testWidth(self):
        """function for testing"""
        obj = Rectangle(5, 7)
        self.assertEqual(obj.width, 5)
        self.assertEqual(obj.height, 7)

    def testparameters(self):
        """function for testing parameters"""
        obj = Rectangle(5, 7, 3, 4)
        self.assertEqual(obj.width, 5)
        self.assertEqual(obj.height, 7)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def testArea(self):
        """function for testing area"""
        obj1 = Rectangle(5, 5)
        self.assertEqual(obj1.area(), 25)

    def test_area(self):
        """function for testing area"""
        obj2 = Rectangle(3, 5)
        self.assertEqual(obj2.area(), 15)
    """def test_instance(Self):
        obj3 = Rectangle(3, 5)
        self.assertIsInstance(obj3, Rectangle)"""
