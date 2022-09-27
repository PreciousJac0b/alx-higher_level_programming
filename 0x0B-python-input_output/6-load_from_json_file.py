#!/usr/bin/python3

"""Contains a function that creates an Object from a JSON file"""

import json


def load_from_json_file(filename):
    """
    Creates an Object from the parameter filename file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        new_obj = json.load(f)
    return new_obj
