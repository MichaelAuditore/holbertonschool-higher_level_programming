#!/usr/bin/python3
def magic_calculation(a, b):
    __import__ magic_calculation_102
    from add import add
    from sub import sub
    if a < b:
        c = add(a, b)
        for i in range(c, 90):
            c = add(c , i)
        return c
    return sub(a, b)
