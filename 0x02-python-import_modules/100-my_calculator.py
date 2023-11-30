#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator = (sys.argv[2])
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if operator == '+':
            print(f"{a:d} + {b:d} = {add(a, b):d}".format(add(a, b)))
        elif operator == '-':
            print(f"{a:d} - {b:d} = {sub(a, b):d}".format(sub(a, b)))
        elif operator == '*':
            print(f"{a:d} * {b:d} = {mul(a, b):d}".format(mul(a, b)))
        elif operator == '/':
            print(f"{a:d} / {b:d} = {div(a, b):d}".format(div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
