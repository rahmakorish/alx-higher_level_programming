#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return None
    new = set()
    low = 0
    mul = 0
    sumx = 0
    for setx in my_list:
        low += setx[1]
        mul += (setx[0] * setx[1])
    return mul / low
