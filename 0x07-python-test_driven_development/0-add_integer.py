#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a : The first integer or float value to be added.
        b : The second integer or float value to be added. Defaults to 98.

    Raises:
        TypeError: If `a` or `b` is not an integer or float.

    Returns:
        int: The sum of `a` and `b`, casted to an integer.

    Examples:
        >>> add_integer(5, 3)
        8
        >>> add_integer(2.5, 4.7)
        6
        >>> add_integer(10)
        108
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
