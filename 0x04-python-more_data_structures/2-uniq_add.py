#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return None
    else:
        sum = 0
        num = []
        for x in range(len(my_list)):
            if num in my_list:
                pass
                #num.append(my_list[x])
            elif my_list[x] != num:
                sum += my_list[x]
        return sum
