#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for raw in(matrix):
        for x in range(len(raw)):
            print("{:d}".format(raw[x]* raw[x]),
end ='\n' if x == len(raw)-1 else ' ')
