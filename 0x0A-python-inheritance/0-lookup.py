#!/usr/bin/python3
# 0-lookup
"""lookup module"""


def lookup(obj):
    """
    lookup method
    returns: list of available methods and attributes of an object
    """
    return dir(obj)
