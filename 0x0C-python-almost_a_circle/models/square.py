#!/usr/bin/python3
"""this module implement square class"""
from models.rectangle import Rectangle, Base
"""square class"""


class Square(Rectangle):
    """intial"""
    def __init__(self, size, x=0, y=0, id=None):
        """intializing class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return (self.width)

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """override str"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def to_dictionary(self):
        """dixtionary """
        return{'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

    def update(self, *args, **kwargs):
        """update"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                keysc = {'id', 'size', 'x', 'y'}
                if key in keysc:
                    if key == 'id':
                        self.id = value
                    if key == 'size':
                        self.width = value
                    if key == 'x':
                        self.x = value
                    if key == 'y':
                        self.y = value
