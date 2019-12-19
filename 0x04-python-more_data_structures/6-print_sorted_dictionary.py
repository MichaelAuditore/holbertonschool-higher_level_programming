#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if len(a_dictionary) != 0:
        OrderByKeys = sorted(a_dictionary.keys())
        for i in OrderByKeys:
            print("{}: {}".format(i, a_dictionary[i]))
