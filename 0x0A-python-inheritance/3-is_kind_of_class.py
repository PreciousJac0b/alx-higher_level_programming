#!/usr/bin/python3

"""Contains a python class comparison function"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a_class
    or an instance of a_class superclass
    """
    return isinstance(obj, a_class)
