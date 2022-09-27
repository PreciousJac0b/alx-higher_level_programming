#!/usr/bin/python3

"""Appends a string after some lines in a file"""


def append_after(filename="", search_string="", new_string=""):
    """
    Checks if the lines in a particular file contains search string

    Appends new_string to the end of a line if it does contain it
    """
    r_string = ""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            r_string += line
            if search_string in line:
                r_string += new_string
    with open(filename, 'w', encoding="utf-8") as fd:
        fd.write(r_string)
