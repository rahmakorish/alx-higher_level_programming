#!/usr/bin/python3
""" 1-main """
from rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(-2,10)
    print(r1.width)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.width, r3.height, r3.x, r3.y)

