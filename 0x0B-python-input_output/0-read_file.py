#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """" reads a file and prints to stdout
    args
       filename: name of file to read (default "")
    """
    with open(filename, 'r', encoding="UTF8") as f:
        read_data = f.read()
        print(read_data, end='')
