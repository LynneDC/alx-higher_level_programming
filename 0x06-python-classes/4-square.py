#!/usr/bin/python3
# 4-square.py
"""defines a class called square """


class Square:

    def __init__(self, size=0):
        self.__size = size
    """gets the size"""
    @property
    def size(self):
        return self.__size
    """gets the value"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
