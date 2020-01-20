#!/usr/bin/python3
def lookup(obj):
    """
    function that returns the list of available attributes
    and methods of an object
    """
    ls = []
    for att in dir(obj):
        ls.append(att)
    return ls
