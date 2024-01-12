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
    def test_id(self):
        self.assertIsNotNone(id)
    def test_nums_id(self):
        obj = Base(4)
        self.assertEqual(obj.id, 4)
    def test_increment(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
    def test_none_id (self):
        obj = Base(id=None)
        self.assertEqual(obj.id, 3)
