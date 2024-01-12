#!/usr/bin/python3
""" class Base"""


class Base:
    """private class attribute"""
    __nb_objects = 0

    """class constructor"""
    def __init__(self, id=None):
        """init method"""
        if (id != None):
            self.id = id
        elif (id == None):
            Base.__nb_objects += 1
            self.id = self.__nb_objects


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
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value
    @property
    def width(self):
        return self.__width

    @property
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value
    @property
    def height(self):
        return self.__height
    
    @property
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    @property
    def x(self):
        return self.__x

    @property
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    @property
    def y(self):
        return self.__y

    @property
    def area(self):
        """rectangle area"""
        return (self.width * self.height)
    
    @property
    def __str__(self):
        return f'[Rectangle] ({self.id:d}) {self.x:d}/{self.y:d} - {self.width:d}/{self.height:d}'
    @property
    def display(self):
        """ocerride str"""
        shape = ""
        if self.__width == 0 or self.__height == 0:
            return shape
        for x in range(0, self.__height):
            shape += ('#' * self.__width)
            if x != self.height - 1:
                shape += "\n"
        return shape

