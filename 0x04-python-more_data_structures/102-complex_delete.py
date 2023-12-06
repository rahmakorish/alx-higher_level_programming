#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return
    else:
        new = a_dictionary.copy()
        for y, x in a_dictionary.items():
            if x == value:
                new.pop(y)
        return new
