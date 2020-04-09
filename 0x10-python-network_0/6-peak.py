#!/usr/bin/python3
""" find the peak
"""


def rec_peak(lbegin, last, l):
    """ search peak into list of integers  """
    mid = (lbegin + last)

    if (mid % 2 == 0):
        m = int(mid / 2)
    else:
        m = int((mid - 1) / 2)
    if (m == 0 or l[m] >= l[m - 1]) and (m == last - 1 or l[m] >= l[m + 1]):
        return (l[m])
    elif (m > 0 and l[m] < l[m - 1]):
        return (rec_peak(lbegin, m, l))
    elif (m < last - 1 and l[m] < l[m + 1]):
        return (rec_peak(m, last, l))
    else:
        return(None)


def find_peak(list_of_integers):
    """ function that get the peak from a list of integers"""
    if not list_of_integers:
        return (None)

    l = list_of_integers
    return (rec_peak(0, len(l), l))
