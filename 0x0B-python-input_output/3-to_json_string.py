#!/usr/bin/python3

"""returns the string json representation of an object"""

import json


def to_json_string(my_obj):
    """returns the string representation of object passed to it"""
    return json.dumps(my_obj)
