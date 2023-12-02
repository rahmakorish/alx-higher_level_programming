#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = my_list.copy()
    for x in range(0, len(my_list)):
        if my_list[x] % 2 == 0:
            new[x] = True
        else:
            new[x] = False
    return (new)
