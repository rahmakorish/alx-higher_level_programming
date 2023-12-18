#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        try:
            if i == x - 1:
                count += 1
                print("{:d}".format(my_list[i]), end = "\n")
            else:
                count += 1
                print("{:d}".format(my_list[i]), end = '')
        except (TypeError, ValueError):
            count -= 1 
            pass
    return count
