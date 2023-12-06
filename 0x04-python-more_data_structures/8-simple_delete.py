#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is None:
        return
    else:
        for x in a_dictionary.keys():

            if x == key:
                a_dictionary.pop(key)
        return a_dictionary
