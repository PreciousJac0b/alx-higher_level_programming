#!/usr/bin/python3
"""
This module provides a function that
finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """Returns the peak value in the list"""
    if type(list_of_integers).__name__ != 'list':
        return
    if len(list_of_integers) == 0:
        return
    list_of_integers.sort()
    return list_of_integers[-1]