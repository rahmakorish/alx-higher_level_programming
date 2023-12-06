#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is None:
        return
    else:
        new = a_dictionary.copy()
        for x in a_dictionary.keys():
            if x == key:
                new.pop(key)
            else:
                pass
        return new
