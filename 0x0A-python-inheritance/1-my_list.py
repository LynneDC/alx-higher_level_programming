#!/usr/bin/pytyhon3
""" define class"""


class MyList(list):
    """
    a class that inherits from List class and provides additional functionalities
    Public instance method:
        print_sorted: prints the list in ascending order
    """
    def print_sorted(self):
        
        print(sorted(self))
