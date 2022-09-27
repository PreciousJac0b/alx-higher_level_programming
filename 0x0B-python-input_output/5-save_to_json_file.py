#!/usr/bin/python3

"""
Contains a module that writes an Object to a text file
using JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file using JSON
    representation

    Args:
        my_obj: Object to be written
        filename: file to be written to
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
