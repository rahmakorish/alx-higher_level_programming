#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    new = []
    try:
        while count < x:
            new.append(my_list[count])
            count += 1
    except(IndexError, TypeError):
        pass
    print(''.join(map(str, new)))
    return count
