import unittest

#!/usr/bin/python3
from test_base import Base
""" class Base"""


class Rectangle(Base):
    """class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """rectangle area"""
        return (self.__width * self.__height)

    def __str__(self):
        return f'[Rectangle] ({self.id:d}) {self.x:d}/{self.y:d} - {self.width:d}/{self.height:d}'

    def to_dictionary(self):
        return dict()

    def display(self):
        """ocerride str"""
        shape = ""
        if self.__width == 0 or self.__height == 0:
            for z in range(0,self.__y):
                shape += (" " * self.__x)
        for k in range(0, self.__height):
            for z in range(0,self.__y):
                shape = (" " * self.__x)
                if z != self.__y - 1:
                    shape = "\n"
            shape += ('#' * self.__width)
            if k != self.__height - 1:
                shape += "\n"
        print(shape)

    def update(self, *args, **kwargs):
        attributes = [self.__width,self.__height,self.__x,self.__y]
        count = len(args)
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        elif kwargs != None:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value

class testingRectangle(unittest.TestCase):
    def testWidth(self):
        obj = Rectangle(5,7)
        self.assertEqual(obj.width, 5)
        self.assertEqual(obj.height, 7)
    def testparameters(self):
        obj = Rectangle(5,7, 3, 4)
        self.assertEqual(obj.width, 5)
        self.assertEqual(obj.height, 7)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)
    def testArea(self):
        obj1 = Rectangle(5, 5)
        self.assertEqual(obj1.area(), 25)
    def test_area(self):    
        obj2 = Rectangle(3, 5)
        self.assertEqual(obj2.area(), 15)
    """def test_instance(Self):
        obj3 = Rectangle(3, 5)
        self.assertIsInstance(obj3, Rectangle)"""
