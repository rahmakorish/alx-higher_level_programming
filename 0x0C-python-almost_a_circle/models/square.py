#!/usr/bin/python3
from rectangle import Rectangle, Base
"""square class"""


class Square(Rectangle):
    """intial"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y)
        Rectangle.height = Rectangle.width
        self.size = Rectangle.width
        #super().__init__(width)
    @property
    def size(self):
        return (self.size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be > 0")
        self.size = value

    def __str__(self):
        return f'[Square] ({self.id:d}) {self.x:d}/{self.y:d} - {self.width:d}'

