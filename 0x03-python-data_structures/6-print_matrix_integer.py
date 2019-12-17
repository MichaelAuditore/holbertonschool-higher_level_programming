#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    idx = 0
    for i in matrix:
        for a in i:
            if a != i[-1]:
                print("{:d}".format(a), end=" ")
            else:
                print("{:d}".format(a), end="")
            print()
