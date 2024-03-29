#!/usr/bin/python3
"""this module xontain class"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """rectangle area"""
        return (self.__width * self.__height)

    def __str__(self):
        """override str function"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height))

    def to_dictionary(self):
        """print dictionary"""
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}

    def display(self):
        """override display()"""
        print("\n" * self.__y, end="")
        line = " " * self.__x + "#" * self.__width + '\n'
        print(line * self.__height, end="")

    def update(self, *args, **kwargs):
        """update()"""
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
        elif kwargs:
            keysx = {'id', 'width', 'height', 'x', 'y'}
            for key, value in kwargs.items():
                if key in keysx:
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
