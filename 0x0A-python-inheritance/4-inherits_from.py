#!/usr/bin/python3
"""class inheretence"""


def inherits_from(obj, a_class):
    """class"""
    x = isinstance(obj, a_class)
    if x:
        return True
    return False
