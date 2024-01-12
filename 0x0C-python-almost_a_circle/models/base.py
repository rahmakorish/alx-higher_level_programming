#!/usr/bin/python3
""" class Base"""


class Base:
    __nb_objects = 0

    """class constructor"""
    def __init__(self, id=None):
        """init method"""
        if (id is not None):
            self.id = id
        elif (id is None):
            Base.__nb_objects += 1
            self.id = self.__nb_objects
