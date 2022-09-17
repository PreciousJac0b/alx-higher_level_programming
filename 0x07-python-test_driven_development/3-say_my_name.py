#!/usr/bin/python3
"""
    Contains a function that prints the first
    and last name inputted
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a name

    Args:
        first_name (string): First name to be printed
        last_name (string): Last name to be printed

    Raises:
        TypeError: if first_name or last_name
        isn't a string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
