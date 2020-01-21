#!/usr/bin/python3
import json


def from_json_string(my_str):
    """
    function that returns an Object representation of a JSON string
    """
    return json.loads(my_str)
