#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """
    function that creates an object from a "JSON File"
    returns the object
    """
    obj = ""
    with open(filename, "r") as f:
        obj = json.load(f)
    f.closed
    return obj
