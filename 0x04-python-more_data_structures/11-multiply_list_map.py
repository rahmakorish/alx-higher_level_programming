#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    def mult(x):
        return x * number
    result = map(mult, my_list)
    return result
