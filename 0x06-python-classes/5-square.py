#!/usr/bin/python3


class Square:
    """This class represents a square."""

    def __init__(self, size):
        """Initializes a new Square object."""
        self.size = size
    """gets the size of square"""
    @property
    def size(self):
        return (self.__size)
    """gets the value """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """prints the square using the '#' character."""
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

        else:
            print()
