#!/usr/bin/python3

"""
Returns the dictionary description of a simple
data structure
"""


def class_to_json(obj):
    """Returns dictionary description of a data structure"""
    return obj.__dict__
