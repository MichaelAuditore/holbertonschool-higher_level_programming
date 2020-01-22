#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """
    save an object into text file in JSON representation
    Returns nothing
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
    f.closed
