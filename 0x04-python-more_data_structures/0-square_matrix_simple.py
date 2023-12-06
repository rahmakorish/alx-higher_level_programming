#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    new = []
    for raw in(matrix):
        for x in range(0, (len(raw))):
            new[x] = raw[x] * raw[x]            
            
    return new
            #print("{:d}".format(raw[x]* raw[x]),
#end ='\n' if x == len(raw)-1 else ' ')
