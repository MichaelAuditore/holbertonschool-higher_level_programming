#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """
    save an object into text file in JSON representation
    Returns nothing
    """
    x = json.dumps(my_obj)
    with open(filename, "w") as f:
        f.write(x)
    f.closed
