#!/usr/bin/python3
def uppercase(str):
    for c in range(0, (len(str))):
        x = ord(str[c])
        if x < 123 and x > 96:
            x = x - 32
            print(f"chr(x)", end="")
        else:
            x 
            print(f"{:c}",str[c], end="")
