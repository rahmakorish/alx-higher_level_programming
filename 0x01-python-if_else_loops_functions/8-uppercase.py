#!/usr/bin/python3
def uppercase(str):
    for c in range(0, (len(str))):
        x = ord(str[c])
        if x < 123 and x > 96:
            x = x - 32
            print(chr(x), end="")
        else:
            print(chr(x), end="")
