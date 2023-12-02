#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new = []
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        for x in range(0, len(my_list)):
            if idx == x:
                my_list.remove(my_list[x])
            else:
                pass
    return (my_list)
