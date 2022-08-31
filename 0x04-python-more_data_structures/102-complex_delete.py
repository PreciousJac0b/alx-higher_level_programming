#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    if not value or value not in a_dictionary.values():
        return a_dictionary
    for elem in list(a_dictionary):
        if a_dictionary[elem] == value:
            del a_dictionary[elem]
    return a_dictionary
