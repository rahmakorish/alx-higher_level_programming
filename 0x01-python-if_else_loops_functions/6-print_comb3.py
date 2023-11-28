#!/usr/bin/python3
for i in range(0, 10):
    for x in range(0, 10):
        if (x == i):
            pass
        elif int(f"{i:d}{x:d}") > int(f"{x:d}{i:d}"):
            pass
        elif int(f"{i:d}{x:d}") == 89:
            print(f"{i:d}{x:d}".format(i).format(x), end="\n")
        else:
            print(f"{i:d}{x:d}, ".format(i).format(x), end="")
