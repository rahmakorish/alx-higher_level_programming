#!/usr/bin/python3
"""class inheretence"""

class list:
    def lookup(obj):
        """class"""
        return list(dir(obj))

class MyList(list):
    """class inheretence"""
    def __init__(self):
        list.__init__(self)

    def print_sorted(self):
        return (sorted(self.lookup()))

