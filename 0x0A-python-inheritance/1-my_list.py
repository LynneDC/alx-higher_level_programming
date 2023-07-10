#!/usr/bin/pytyhon3
"""module inherits from list class"""


class MyList(list):
    """
    a class that inherits from List
    Public instance method:
        print_sorted: prints the list in ascending order
    """
    def print_sorted(self):

        print(sorted(self))
