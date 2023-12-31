#!/usr/bin/python3
"""python rectangle class"""


class Rectangle:
    """new class"""
    def __init__(self, width=0, height=0):
        """constructor."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter function for width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setter for width"""
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter function for height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setter for heigth"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """function to return squarea area"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * self.__height)

    def perimeter(self):
        """function to return rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            perimet = 0
            return (perimet)
        perimet = (self.__width + self.__height) * 2
        return (perimet)
