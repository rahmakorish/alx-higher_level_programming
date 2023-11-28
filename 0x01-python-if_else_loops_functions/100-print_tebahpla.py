#!/usr/bin/python3
def rev_alpha():
    for x in range(90, 64, -1):
        if x % 2 == 0:
            x += 32
        print(f"{x:c}".format(x), end="")


rev_alpha()
