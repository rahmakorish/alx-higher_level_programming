#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 is None:
        return
    if set_2 is None:
        return
    else:
        new = set_1.symmetric_difference(set_2)
    return (new)
