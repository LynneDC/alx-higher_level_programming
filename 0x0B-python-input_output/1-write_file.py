#!/usr/bin/python3
"""contain module to write to the file"""


def write_file(filename="", text=""):
    """write to the file and also returns number of chars read
    args:
        filename: (str) file to write to (default "")
        text: (str) the content to write to file (default "")
    Returns:  number of characters added
    """
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)
