#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    num1 = 0
    num2 = 0
    if len(tuple_a) >= 2 & len(tuple_b) >= 2:
        num1 = tuple_a[0] + tuple_b[0]
        num2 = tuple_a[1] + tuple_b[1]
    elif 1 <= len(tuple_b) < 2:
        num1 = tuple_b[0] + tuple_a[0]
        num2 = 0 + tuple_a[1]
    elif len(tuple_b) == 0:
        num1 = 0 + tuple_a[0]
        num2 = 0 + tuple_a[1]
    new = (num1, num2)
    return (new)
