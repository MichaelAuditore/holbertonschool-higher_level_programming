#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()
    else:
        idx = 0
        for i in matrix:
            for a in i:
                if a != i[-1]:
                    print("{:d}".format(a), end=" ")
                else:
                    print("{:d}".format(a))
