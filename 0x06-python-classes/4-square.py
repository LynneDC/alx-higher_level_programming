#!/usr/bin/python3
# 4-square.py
"""defines a class called square """


class Square:
    """represent a square"""
    def __init__(self, size=0):
        """
        initilizes a new square
        args:
        size(int): the size of new square
        """
        self.size = size
    """gets the size of square"""
    @property
    def size(self):
        return self.__size
    """gets the value"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size * self.__size)
