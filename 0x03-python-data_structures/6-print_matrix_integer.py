#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for raw in matrix:
        if raw is None:
            return
        lenr = len(raw) - 1
        for x in range(0, len(raw)):
            print("{:d}".format(raw[x]), end='\n' if x == lenr else ' ')
