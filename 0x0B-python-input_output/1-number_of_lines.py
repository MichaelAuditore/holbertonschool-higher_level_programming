#!/usr/bin/python3
def number_of_lines(filename=""):
    """
    function that returns number of lines of a file
    """
    nlines = 0
    with open(filename, "r") as f:
        for line in f:
            nlines += 1
    f.closed
    return nlines
