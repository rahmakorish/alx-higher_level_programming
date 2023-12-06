#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        new = {}
        for x, y in a_dictionary.items():
            new.update({x: y * 2})
        return new
