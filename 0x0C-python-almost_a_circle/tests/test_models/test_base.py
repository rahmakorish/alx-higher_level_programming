#!/usr/bin/python3
import unittest

class Base:
    __nb_objects = 0

    """class constructor"""
    def __init__(self, id=None):
        """init method"""
        if (id != None):
            self.id = id
        elif (id == None):
            Base.__nb_objects += 1
            self.id = self.__nb_objects


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
