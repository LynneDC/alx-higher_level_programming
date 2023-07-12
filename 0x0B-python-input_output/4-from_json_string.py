#!/usr/bin/python3
"""json module"""
import json


def from_json_string(my_str):
    """returns an object represented by a json string
    args:
        my_str: the string to be returned
    """
    return json.dumps(my_str)
