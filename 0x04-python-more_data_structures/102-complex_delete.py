#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return
    else:
        for y, x in a_dictionary.items():
            if x == value:
                a_dictionary.pop(y)
        return a_dictionary
