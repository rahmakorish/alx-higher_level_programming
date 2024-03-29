#!/usr/bin/python3
""" class Base"""
import json


class Base:
    """class"""
    __nb_objects = 0

    """class constructor"""
    def __init__(self, id=None):
        """init method"""
        if (id is not None):
            self.id = id
        elif (id is None):
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string"""
        if json_string is None or len(json_string) == 0:
            return '{}'
        return (json.loads(json_string))
