#!/usr/bin/python3
"""this test module"""
import unittest
import os.path
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""tests the Base"""


class BaseTest(unittest.TestCase):
    """class for testing Base"""

    def test_id(self):
        """test id"""
        self.assertIsNotNone(id)

    def test_nums_id(self):
        """test id"""
        obj = Base(4)
        self.assertEqual(obj.id, 4)

    def test_increment(self):
        """test id"""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_none_id(self):
        """test id"""
        obj = Base(id=None)
        self.assertEqual(obj.id, 3)
