#!/usr/bin/python3
def no_c(my_string):
    new_list = ""
    for x in range(0, len(my_string)):
        if my_string[x] == 'c' or my_string[x] == 'C':
            pass
        else:
            new_list += my_string[x]
    return new_list
