#!/usr/bin/python3

"""
Defines a function that prints a square
with the string '#'
"""


def print_square(size):
    """
    Prints a square with the # string

    Args:
        size (int): length and breadth of square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size less than zero
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
