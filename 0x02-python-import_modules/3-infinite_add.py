#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sumx = 0
    count = len((sys.argv))
    for i in range(1, count):
        if sys.argv[i]:
            num = int(sys.argv[i])
            sumx += num
    print(f"{sumx:d}".format(sumx))
