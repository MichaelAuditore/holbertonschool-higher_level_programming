#!/usr/bin/python3


def class_to_json(obj):
    """
    Convert a class in json
    """
    d = {}
    if hasattr(obj, "__dict__"):
        d = obj.__dict__.copy()
    return d
