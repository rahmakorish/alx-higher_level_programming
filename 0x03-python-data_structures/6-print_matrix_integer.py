#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for raw in matrix:
        for x in range(0, len(raw)):
            print("{:d}".format(raw[x]),end = '\n' if x == len(raw) - 1 else ' ')
