#!/usr/bin/python3
from rectangle import Rectangle, Base
"""square class"""


class Square(Rectangle):
    """intial"""
    def __init__(self, size, x=0, y=0, id=None):
        """intializing class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.width = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        return{'id':self.id,'x':self.x, 'size':self.size, 'y':self.y}

    def update(self, *args, **kwargs):
        if args:
            c = len(args)
            if c >= 1:
                self.id = args[0]
            if c >= 2:
                self.width = args[1]
            if c >= 3:
                self.x = args[2]
            if c >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.width = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
