#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        for x in range(0, len(my_list)):
            if x == idx:
                my_list[x] = element
            else:
                pass
    return (my_list)
