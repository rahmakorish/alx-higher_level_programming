#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = len((sys.argv)) - 1
    if count == 0:
        print(f"{count:d} arguments.".format(count))
    elif count == 1:
        print(f"{count:d} argument:".format(count))
        for i in range(1, len(sys.argv)):
            print(f"{i:d}: {sys.argv[i]:}".format(i).format(sys.argv[i]))
    else:
        print(f"{count:d} arguments:".format(count))
        for i in range(1, len(sys.argv)):
            print(f"{i:d}: {sys.argv[i]:}".format(i).format(sys.argv[i]))
