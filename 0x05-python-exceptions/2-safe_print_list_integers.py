#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    new = []
    try:
        for i in range (0, x):
            if my_list[i].isdigit():
                new.append(my_list[i])
                count += 1
    except (TypeError, ValueError):
        pass
        #count -= 1
    print("".join(map(str,new)))
    return (count)
