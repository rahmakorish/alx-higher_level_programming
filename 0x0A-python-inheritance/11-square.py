#!/usr/bin/python3
""" class Base"""
from rectangle import Rectangle


class Square(Rectangle):
    """class Square"""


    def __init__(self, size):
        """init method"""
        self.size = size

    @property
    def area(self):
        """square area"""
        return (size * size)

    @property
    def print(self):
        """print format"""
        print("[Square] {:d}/{:d}".format(self.size,self.size))

    def __str__(self):
        """print format"""
        return "[Square] {:d}/{:d}".format(self.size,self.size)

