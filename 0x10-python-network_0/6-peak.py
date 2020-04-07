#!/usr/bin/env python3
""" module to find peak in a list of integers """


def find_peak(list_of_integers):
    """find peak in a list of integers"""
    if len(list_of_integers) == 0:
        return (None)
    elif len(list_of_integers) == 1:
        return (list_of_integers[0])
    else:
        for idx in range(1, len(list_of_integers)):
            cur = list_of_integers[idx]
            for number in range(idx + 1):
                prev = list_of_integers[idx - 1]
                if ((idx + 1) <= len(list_of_integers) - 1):
                    after = list_of_integers[idx + 1]
                else:
                    after = 0
                if (prev <= cur and after <= cur):
                    peak = cur
        return (peak)
