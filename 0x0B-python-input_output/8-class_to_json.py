#!/usr/bin/python3

"""
Returns the dictionary description of a simple
data structure
"""

import json


def class_to_json(obj):
    """Converts class object to json"""
    return json.dumps(obj.__dict__)
