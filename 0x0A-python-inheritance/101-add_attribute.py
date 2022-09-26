#!/usr/bin/python3

"""Represents a class"""


def add_attribute(first, second, third):
    """
    Adds attribute to a class if possible
    """
    if not hasattr(first, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(first, second, third)
