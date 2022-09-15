#!/usr/bin/python3

"""
This is a two integer addition module

The add integer module supplies one function, add_integer(a, b)

Returns the result of the addition of two ints or float numbers

The result returned is typecasted into an int
"""


def add_integer(a, b=98):
    """
    Returns the addition of two integers, an exact integer

    Float types are type casted to integers before addition

    Raises:
            TypeError if arguments passed isn't a float or an int
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
