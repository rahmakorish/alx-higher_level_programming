#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 is None:
        return None
    if set_2 is None:
        return None
    else:
        new = set()
        for x in set_1:
            for i in set_2:
                if x == i:
                    new.add(x)
        return new
