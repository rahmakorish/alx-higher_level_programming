#!/usr/bin/python3
def matrix_divided(matrix, div):
    new = []
    try:
        for x in matrix:
            for i in x:
                i = round(i / div,2)
                new.append(i)
    except TypeError:
        raise ("matrix must be a matrix (list of lists) of integers/floats")
    return new
