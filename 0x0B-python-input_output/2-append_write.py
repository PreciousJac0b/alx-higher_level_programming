#!/usr/bin/python3

"""Opens a file in append mode and writes to it"""


def append_write(filename="", text=""):
    """Opens a file in append mode and writes to it"""
    with open(filename, 'a') as f:
        new_file = f.write(text)
    return new_file
