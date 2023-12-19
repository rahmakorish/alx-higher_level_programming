#!/usr/bin/python3
"""python file"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        self._size = size
    """getter function for size"""
    @property
    def size(self):
        return (self._size)
    """setter function for size"""
    @size.setter
    def size(self, value):
        self._size = value
        if not type(self._size) is int or not type(self._size) is float:
            raise TypeError("size must be a number")
        if self._size < 0:
            raise ValueError("size must be >= 0")
    """function to return squarea area"""
    def area(self):
        sizex = self._size
        return (int(sizex * sizex))
    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()
        return False
