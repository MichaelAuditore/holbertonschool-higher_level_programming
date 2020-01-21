#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    append something that we want to write into a file
    """
    nb_lines = 0
    with open(filename, "a") as f:
        nb_lines = f.write(text)
    f.closed
    return nb_lines
