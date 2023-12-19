#!/usr/bin/python3
"""pyrhon file """


class Square:
    """a class Square that defines a square"""
    def __init__(self, size=0):
        """constructor.
        Args:
            size:square size
            """
        self.size = size
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
