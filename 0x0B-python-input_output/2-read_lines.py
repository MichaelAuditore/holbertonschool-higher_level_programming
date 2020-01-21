#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """
    this function read lines by nb_lines, if
    nb_lines <= 0 read entire file
    """
    with open(filename, "r") as f:
        if nb_lines <= 0:
            for line in f:
                print(line, end="")
        else:
            for i in range(0, nb_lines):
                print(f.readline(), end="")
