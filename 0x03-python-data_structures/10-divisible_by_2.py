#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    idx = 0
    if my_list is None or len(my_list) == 0:
        return False
    for i in my_list:
        if (i % 2 == 0):
            new_list[idx] = True
        else:
            new_list[idx] = False
        idx += 1
    return new_list
