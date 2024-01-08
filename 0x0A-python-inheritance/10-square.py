#!/usr/bin/python3
"""base class"""


class BaseGeometry:
    """class"""
    def __init__(self):
        """class"""
    def area(self):
        """class method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """class method"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """class"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height


class Square:
    """class"""
    def __init__(self, size):
        """class method"""
        self.__size = size

    def area(self):
        """class method"""
        return (self.__size * self.__size)
