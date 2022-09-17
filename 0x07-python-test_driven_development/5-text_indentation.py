#!/usr/bin/python3

"""
Defines a text indentation python function
"""


def text_indentation(text):
    """
    A text indentation function
    Prints a text with 2 indentation after characters
    in the string ".?:"

    Args:
        text (string):  text to be indented

    Raises:
        TypeError: text must be a string if text
        is not a string
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    codex = ".?:"
    for elem in text:
        if elem in codex:
            print("{}".format(elem))
            print()
        else:
            print("{}".format(elem), end="")
