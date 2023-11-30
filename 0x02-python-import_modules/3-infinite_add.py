#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = 0
    count = len((sys.argv)) - 1
    for i in range (1, count):
        num = int(sys.argv[i])
        count += num
    print(f"{count:d}".format(count))
