#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix

    Parameters:
             matrix: list of list of type integer or float
             div: Number greater than 0 to divide each element of matix

    TypeError:
             matrix must be a matrix (list of lists) of integers/floats
             Each row of the matrix must have the same size
             div must be a number

    ZeroDivisionError:
             division by zero

    Returns:
    New matrix with the result of divide each element by div

    """
    typemsg = "matrix must be a matrix (list of lists) of integers/floats"
    rowmsg = "Each row of the matrix must have the same size"

    idx = 0
    tmp = 0

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not matrix or type(matrix) is not list:
        raise TypeError(typemsg)

    for i in matrix:

        if type(i) is not list or not i:
            raise TypeError(typemsg)

        if idx == 0:
            tmp = len(i)
        else:
            if tmp != len(i):
                raise TypeError(rowmsg)
        for s in i:
            if type(s) is not int and type(s) is not float:
                raise TypeError(typemsg)
        idx += 1

    nm = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (nm)
