#!/usr/bin/python3
import sys
"""python N queen"""

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
for i in range(0, len(sys.argv)):
    if not int(sys.argv[1]):
        print("N must be a number")
        exit(1)
    elif int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)
    else:
        print(sys.argv[1])
