#!/usr/bin/python3
""" module to find peak in a list of integers """


def find_peak(list_of_integers):
    """find peak in a list of integers"""
    if list_of_integers is None or len(list_of_integers) == 0:
        return (None)
    else:
        p = list_of_integers[0]
        for number in list_of_integers:
            if number > p:
                p = number
        return p
