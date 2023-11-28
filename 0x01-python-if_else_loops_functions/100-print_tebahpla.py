#!/usr/bin/python3
def rev_alpha():
    for x in range(90, 64, -1):
        if x % 2 == 0:
            x += 32
            print(f"{x:c}", end="")
        else:
            print(f"{x:c}", end="")


rev_alpha()
