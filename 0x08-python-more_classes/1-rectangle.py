#!/usr/bin/python3
"""python rectangle class"""


class Rectangle:
    """new class"""
    def __init__(self, width=0, height=0):
        """constructor."""
        self.__width = width
        self.__height = height
    # """getter function for width"""
    @property
    def width(self):
        """getter function for width"""
        return (self.__width)
    # """setter for width"""
    @width.setter
    def width(self, value):
        """setter for width"""
        # self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
   # """getter function for height"""
    @property
    def height(self):
    """setter for heigth"""
        return (self.__height)
   # """setter for heigth"""
    @height.setter
    def height(self, value):
        """setter for heigth"""
        # self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
