#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
if __name__ == "__main__":
    print(f"{a:d} + {b:d} = {add(a, b):d}".format(add(a, b)))
    print(f"{a:d} - {b:d} = {sub(a, b):d}".format(sub(a, b)))
    print(f"{a:d} * {b:d} = {mul(a, b):d}".format(mul(a, b)))
    print(f"{a:d} / {b:d} = {div(a, b):d}".format(div(a, b)))
