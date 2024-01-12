import unittest
#!/usr/bin/python3
from test_rectangle import Rectangle, Base
"""square class"""


class Square(Rectangle):
    """intial"""
    def __init__(self, size, x=0, y=0, id=None):
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
        #self.height = value
        #self.size = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    def to_dictionary(self):
        return dict()
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


class Test_square(unittest.TestCase):
    """class for testing square"""
    def test_attributes(self):
        """function to test attributes"""
        obj = Square(3, 4, 6)
        self.assertEqual(obj.size, 3)
        self.assertEqual(obj.x, 4)
        self.assertEqual(obj.y, 6)

    def test_area(self):
        """function to test area()"""
        obj = Square(3)
        self.assertEqual(obj.area(), 9)
        obj1 = Square(4)
        self.assertEqual(obj1.area(), 16)

    def test_update(self):
        """function to test update()"""
        obj = Square(3, 4, 6)
        self.assertEqual(obj.size, 3)
        self.assertEqual(obj.x, 4)
        self.assertEqual(obj.y, 6)
        obj.update(1, 2, 3)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 6)
