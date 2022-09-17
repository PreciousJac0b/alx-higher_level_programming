#!/usr/bin/python3
"""
Defines a matrix division function
"""


def matrix_divided(matrix, div):
    """
    Matrix function that divides all element in a matrix by the
    div parameter

    Args:
        matrix (list): Matrix to be transformed by division
        div (int): Divisor.

    Raises:
        TypeError if div is not a number
        ZeroDivisionError if div is zero
        TypeError if matrix doesn't consist equal length list
        TypeError if matrix doesn't elements of type int or float

    Returns:
        A new matrix representing the result of division.
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")
    else:
        new_matrix = []
        for elem in matrix:
            if type(elem) != list:
                raise TypeError("matrix must be a matrix (list"
                                "of lists) of integers/floats")
            elif len(elem) != len(matrix[0]):
                raise TypeError("Each row of the matrix must"
                                "have the same size")

            append_matrix = []
            for elements in elem:
                if type(elements) not in [int, float]:
                    raise TypeError("matrix must be a matrix (list of lists)"
                                    "of integers/floats")
                else:
                    append_matrix.append(round(elements/div, 2))
            new_matrix.append(append_matrix)
    return new_matrix
