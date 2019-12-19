#!/usr/bin/python3
def number_keys(a_dictionary):
    if a_dictionary is None:
        return 0
    else:
        add = 0
        for i in a_dictionary:
            add += 1
        return add
