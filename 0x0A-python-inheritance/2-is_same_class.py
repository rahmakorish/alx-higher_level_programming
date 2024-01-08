#!/usr/bin/python3
"""class inheretence"""


def is_same_class(obj, a_class):
    """class"""
    x = isinstance(obj, a_class)
    if x:
        return True
    return False
