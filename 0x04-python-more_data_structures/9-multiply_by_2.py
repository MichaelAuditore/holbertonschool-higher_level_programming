#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    if len(a_dictionary) != 0:
        OrderByKeys = sorted(a_dictionary.keys())
        for i in OrderByKeys:
            new[i] = a_dictionary[i] * 2
        return new
