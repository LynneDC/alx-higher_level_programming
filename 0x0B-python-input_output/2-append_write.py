#!/usr/bin/python3
"""module for appending to a file"""


def append_write(filename="", text=""):
    """appends a string to the end of file
    args:
        filename:(str) name of file to append to (default "")
        text: (str) the characters to append (default "")
    Return:  number of characters added
    """
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
