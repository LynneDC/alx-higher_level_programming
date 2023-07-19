#!/usr/bin/python3
"""module that prints a matrix of same size"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix
    args:
        matrix(list): a list of lists of integers and floats
        div(int, float): a number to divide
    raises:
        TypeError: if div is not in or float
        TypeError: if matrix conatis rows of different size
        ZeroDivision Error:if divis equal to zero
        TypeError: if div is not int or float
    returns:
        new_matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, int) or isinstance(element, float))
                    for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
