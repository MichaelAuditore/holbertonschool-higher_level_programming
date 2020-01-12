#!/usr/bin/python3
def print_square(size):
    """
    Print a square using # symbols to paint it

    Parameters:
           Size: Is a Integer number who represents the size length of square

    TypeErrors:
           size must be an integer

    ValueErrors:
           size must be >= 0

    Returns:
           Not returns only print a square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    x, y = size, size
    for i in range(x):
        for j in range(y):
            print("#", end="")
        print()
