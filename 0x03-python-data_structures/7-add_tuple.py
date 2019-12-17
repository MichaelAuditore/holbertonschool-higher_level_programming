#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum1 = 0
    sum2 = 0

    if (len(tuple_a) == 0):
        a = 0
        b = 0
    elif (len(tuple_a) == 1):
        a = tuple_a[0]
        b = 0
    else:
        a = tuple_a[0]
        b = tuple_a[1]
    if (len(tuple_b) == 0):
        aa = 0
        bb = 0
    elif (len(tuple_b) == 1):
        aa = tuple_b[0]
        bb = 0
    else:
        aa = tuple_b[0]
        bb = tuple_b[1]
    sum1 = a + aa
    sum2 = b + bb
    tuple_c = (sum1, sum2)
    return tuple_c
