#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    new = []
    for i in range(0, x):
        try:
            new.append(my_list[i])
            count += 1
        except (TypeError, ValueError):
            pass
    print("".join(map(str, new)))
    return count
