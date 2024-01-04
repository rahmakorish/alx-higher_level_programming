#!/usr/bin/python3
"""python rectangle class"""


class Rectangle:
    """new class"""
    def __init__(self, width=0, height=0):
        """constructor."""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter function for width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setter for width"""
        # self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """setter for heigth"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setter for heigth"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
