#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    new =[]
    big = []
    for raw in(matrix):
        for x in range(len(raw)):
                new.append(raw[x] * raw[x])
    return new
