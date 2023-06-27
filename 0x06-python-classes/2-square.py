#!/usr/bin/python3
"""defines a class called square """


class Square:
    """define and initilize using init"""
    def __init__(self, size=0):
        """handle errors"""
        try:
            """check is size is not digit"""
            if type(size) is not int:
                """print out type error message because its expecting int"""
                raise TypeError("size  mustbe an integer")
            """check if size is less tha 0"""
            if size < 0:
                """
                raise a valueerror message because
                the minimum value should be of size 0
                """
                raise ValueError("size must be >= 0")

            
           ""assign value to an object"""
            self.__size = size
