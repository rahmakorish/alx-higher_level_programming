#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for x in range(len(new)):
        if x == search - 1:
            new[x] = replace
        else:
            pass
    return (new)
