#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return 0
    else:
        add = 0
        prev = 0
        my_list.sort()
        for i in my_list:
            if (i != prev):
                add += i
            prev = i
        return add
