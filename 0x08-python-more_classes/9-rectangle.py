#!/usr/bin/python3
"""python rectangle class"""


class Rectangle:
    """new class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """constructor."""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
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
    """height deleter"""
    @height.deleter
    def height(self):
        # self.__width = None
        self.__height = None
        print("Bye rectangle...")

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
    """width deleter"""
    @width.deleter
    def width(self):
        self.__width = None
        print("Bye rectangle...")

    def __del__(self):
        """destryctor"""
        self.__width = None
        self.__height = None
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    def square(cls, size=0):
        cls = Rectangle(cls, cls)
        return cls
