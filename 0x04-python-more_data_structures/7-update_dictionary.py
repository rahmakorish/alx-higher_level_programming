#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None:
        return
    else:
        for x in a_dictionary.keys():
            if key == x:
                a_dictionary[x] = value

        a_dictionary.update({key: value})
