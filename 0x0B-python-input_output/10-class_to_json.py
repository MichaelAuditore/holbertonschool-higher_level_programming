#!/usr/bin/python3
import json


def class_to_json(obj):
    """
    Convert a class in json
    """
    return(obj.__dict__)
