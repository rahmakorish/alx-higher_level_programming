#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        for x in range(0, len(my_list)):
            if x == idx:
                return (my_list[x])
