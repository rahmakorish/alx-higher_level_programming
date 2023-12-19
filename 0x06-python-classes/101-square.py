#!/usr/bin/python3
"""python file"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        self.my_print()
    """getter function for size"""
    @property
    def size(self):
        return (self.__size)
    """setter function for size"""
    @size.setter
    def size(self, value):
        self._size = value
        if not type(self.__size) is int:
            raise TypeError("size must be an integer")
        if self._size < 0:
            raise ValueError("size must be >= 0")
    """retrive position attribute"""
    @property
    def position(self):
        return (self.__position)
    """set position attribute"""
    @position.setter
    def position(self, value):
        self._position = value
        if not type(value) is tuple or not type(value[0]) is int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not type(value[1]) is int or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
    """function to return squarea area"""
    def area(self):
        sizex = self.__size
        return (sizex * sizex)
    """function to print squarea area"""
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
