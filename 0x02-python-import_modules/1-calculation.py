#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
print(f"{a:d} + {b:d} = {add(a, b):d}".format(a).format(b).format(add(a, b)))
print(f"{a:d} - {b:d} = {sub(a, b):d}".format(a).format(b).format(sub(a, b)))
print(f"{a:d} * {b:d} = {mul(a, b):d}".format(a).format(b).format(mul(a, b)))
print(f"{a:d} / {b:d} = {div(a, b):d}".format(a).format(b).format(div(a, b)))
