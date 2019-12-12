__import__ magic_calculation_102
from add import add
from sub import sub
def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for i in range(c, 90):
            c = add(c , i)
        return c
    return sub(a, b)
