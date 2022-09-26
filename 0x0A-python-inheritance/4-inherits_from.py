#!/usr/bin/python3

"""
A function that evaluates subclasses
"""


def inherits_from(obj, a_class):
    """Returns True if obj is a subclass of a_class"""
    if issublass(type(obj), a_class):
        return True
    elif isinstance(obj, a_class):
        return True
    return False
