#!/usr/bin/python3
"""module that imports json"""
import json


def to_json_string(my_obj):
    """returns json representation of an object (string)
    arg:
        my_obj: type object to check
    Returns:
        str: JSON repesentation of abject
    """
    return json.dumps(my_obj)
