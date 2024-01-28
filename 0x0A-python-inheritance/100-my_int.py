#!/usr/bin/python3
"""class"""


class MyInt(int):
    """class rebel"""
    def __arthmatic__(self, num):
        """over ride function"""
        #return not (super().__arthmatic__(num))
        return (self == num)

    """def __equal__(self, num):
        return not super().__equal__(num)"""
