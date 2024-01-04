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
        try:
            self.__width = value
        except TypeError:
            raise "width must be an integer"
        except ValueError:
            raise "width must be >= 0"
    """getter function for width"""
    @property
    def height(self):
        return (self.__height)
    """setter for heigth"""
    @height.setter
    def height(self, value):
        try:
            self.__height = value
        except TypeError:
            raise "height must be an integer"
        except ValueError:
            raise "height must be >= 0"
