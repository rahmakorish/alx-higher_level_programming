#!/usr/bin/python3
from sys import stdin
"""class"""

codes = {"200": 0, '301': 0, '400': 0, '401': 0, '404': 0}
# , '405': 0, '403': 0, '500': 0}

size = i = 0


def printx():
    """function"""
    print(f'file size: {size}')
    for key, value in sorted(codes.items()):
        if value > 0:
            print('{:s}: {:d}'.format(key, value))


try:
    for line in stdin:
        splitline = line.split()
        if len(splitline) >= 2:
            status = splitline[-2]
            size += int(splitline[-1])
            if status in codes:
                codes[status] += 1
        i += 1

        if i % 10 == 0:
            printx()
        printx()
except KeyboardInterrupt as e:
    printx()
