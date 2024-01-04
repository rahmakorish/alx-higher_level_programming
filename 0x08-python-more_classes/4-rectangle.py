#!/usr/bin/python3
"""python rectangle class"""


class Rectangle:
    """new class"""
    def __init__(self, width=0, height=0):
        """constructor."""
        self.__width = width
        self.__height = height
    """getter function for width"""
    @property
    def width(self):
        return (self.__width)
    """setter for width"""
    @width.setter
    def width(self, value):
        self.__width = value
        if not type(self.__width) is int:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
    """getter function for height"""
    @property
    def height(self):
        return (self.__height)
    """setter for heigth"""
    @height.setter
    def height(self, value):
        self.__height = value
        if type(self.__height) is not int:
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
    """function to return squarea area"""
    def area(self):
        return (self.__width * self.__height)
    """function to return rectangle perimeter"""
    def perimeter(self):
        perimet = (self.__width + self.__height) * 2
        return (perimet)
    """function to print"""
    def __str__(self):
        shape = ""
        for x in range(0, self.__height):
            shape += ('#' * self.__width)
            if x != self.height - 1:
                shape += "\n"
        return shape
    """function to print"""
    def __print__(self):
        shape = ""
        for x in range(0, self.__height):
            shape += ('#' * self.__width)
            if x != self.height - 1:
                shape += "\n"
        return shape
    def __repr__(self):
        eval()

