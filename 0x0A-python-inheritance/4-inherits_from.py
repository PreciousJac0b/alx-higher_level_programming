#!/usr/bin/python3

"""
A function that evaluates subclasses
"""


def inherits_from(obj, a_class):
    """Returns True if obj is a subclass of a_class"""
    return type(obj) is not a_class and isinstance(obj, a_class)
