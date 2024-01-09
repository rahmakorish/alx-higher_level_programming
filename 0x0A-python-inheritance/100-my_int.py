#!/usr/bin/python3
"""class"""


class MyInt(int):
    """class rebel"""
    def arthmatic(self, num):
        """over ride function"""
        return not super().__arthmatic__(num)
