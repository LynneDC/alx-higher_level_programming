#!/usr/bin/pytghon3
"""json module  return dict"""
import json


def class_to_json(obj):
    """ returns a dictionary for  json serializeation of an object
    args:
        obj: obj of dict to be returned
    """
    return obj.__dict__
