#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return matrix
    new = []
    idx = 0
    for i in matrix:
        newest = list(map((lambda x: x * x), i))
        new.append(newest)
    return new
