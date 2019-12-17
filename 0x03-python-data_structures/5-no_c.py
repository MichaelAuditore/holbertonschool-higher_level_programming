#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    length = len(my_string)
    idx = 0
    for i in my_string:
        if i == 'c' or i == 'C':
            idx += 1
        else:
            new_str += i
    return new_str
