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
