#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        x = a+b
    except TypeError:
        raise("a must be an integer")
    return x
