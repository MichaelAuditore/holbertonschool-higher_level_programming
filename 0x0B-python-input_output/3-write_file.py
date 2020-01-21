#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    this functions write into a file
    Returns number of characters
    """
    nb_chars = 0
    with open(filename, "w") as f:
        nb_chars = f.write(text)
    f.closed
    return nb_chars
