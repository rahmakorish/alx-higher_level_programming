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
        if not type(self._size) is int:
            raise TypeError("size must be an integer")
        if self._size < 0:
            raise ValueError("size must be >= 0")
    """function to return squarea area"""
    def area(self):
        sizex = self._size
        return (sizex * sizex)
    """function to print squarea area"""
    def my_print(self):
        sqr = self.area()
        if self._size == 0:
            print("")
        else:
            for i in range(0, self._size):
                for x in range(0, self._size+1):
                    if x == self._size:
                        print(end="\n")
                    else:
                        print("#", end='')
