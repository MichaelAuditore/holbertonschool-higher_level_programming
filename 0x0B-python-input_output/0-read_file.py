#!/usr/bin/python3
def read_file(filename=""):
    """
    function to print all into a file
    """
    with open(filename, "r") as f:
        for line in f:
            print(line, end="")
    f.closed
