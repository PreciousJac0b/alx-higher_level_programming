#!/usr/bin/python3

"""
COntains a function that compares a class with its instance
"""


def is_same_class(obj, a_class):
    """
    Checks if the obj parameter
    is an instance of the a_class parameter
    """
    return type(obj) == a_class
