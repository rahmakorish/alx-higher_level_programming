#!/usr/bin/python3
"""python file"""


class Square:
    """a class Square that defines a square"""
    def __init__(self, size=0):
        """constructor.
        Args:
        size:square size"""
        self._size = size
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    """function to find square area"""
    def area(self):
        return (self._size * self._size)
