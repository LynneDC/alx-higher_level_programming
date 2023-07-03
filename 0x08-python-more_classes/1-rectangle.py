#!/usr/bin/python3
# 1-rectangle
"""defines a class called Rectangle """


class Rectangle:
    """represent a square"""

    def __init__(self, width=0, height=0):

        """
        get the width
        with args :
            self, value
        if value is not int or is less than 0
        raise typeerror and value error
        otherwise return the values
        """

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    """
        get the height
        args:
            self,value
        if value is not and int
        or height is less than 0
        raise TypeError and ValueError
        otherwise return the value
    """

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")

        self.__height = value
