#!/usr/bin/python3
"""python rectangle class"""


class Rectangle:
    """new class"""
    def __init__(self, width=0, height=0):
        """constructor."""
        self.width = width
        self.height = height
    """getter function for width"""
    @property
    def width(self):
        return (self.__width)
    """setter for width"""
    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    """getter function for height"""
    @property
    def height(self):
        return (self.__height)
    """setter for heigth"""
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    """function to return squarea area"""
    def area(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * self.__height)
    """function to return rectangle perimeter"""
    def perimeter(self):
        perimet = (self.__width + self.__height) * 2
        return (perimet)
