#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Add_integer functions return the sum of two numbers

    Parameters:
         a: first argument can be integer or float
         b: Second argument initialized with value 98, can be integer or float
    Raises:
         TypeError: a must be an integer or float
         TypeError: b must be an integer or float
    Returns:

    int:Sum of a + b


    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return (a + b)
