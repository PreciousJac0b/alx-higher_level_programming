#!/usr/bin/python3

"""Reads a text file and prints it to stdout"""


def read_file(filename=""):
    """
    Reads and prints a text file UTF8
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
