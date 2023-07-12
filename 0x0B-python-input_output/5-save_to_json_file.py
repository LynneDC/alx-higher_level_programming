#!/usr/bin/python3
"""json module writes to  file"""
import json


def save_to_json_file(my_obj, filename):
    """writes to a file in json representation
    args:
        my_odj: (str) json representation of object
        filename: (str) the file to write to
    """
    with open(filename, 'w', encoding="UTF8") as f:
        json_obj = json.dumps(my_obj)
        f.write(json_obj)
