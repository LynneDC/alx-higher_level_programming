#!/usr/bin/python3
"""module json  that creates object"""
import json


def load_from_json_file(filename):
    """creates an object from json file
    args:
        filename:(str) the file in which the object is being created
    """
    with open(filename,  'r', encoding="UTF8") as f:
        return json.load(f)
