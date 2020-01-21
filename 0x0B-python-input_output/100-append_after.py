#!/usr/bin/pyhon3
def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file,
    after each line containing a specific string
    """
    s = ""
    with open(filename, "r") as f:
        for line in f:
            s += line
            if search_string in line:
                s += new_string
    with open(filename, "w") as f:
        f.write(s)
