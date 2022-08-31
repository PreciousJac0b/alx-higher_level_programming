#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    result = 0
    key = ""
    for elem in a_dictionary.keys():
        if a_dictionary[elem] > result:
            result = a_dictionary[elem]
            key = elem
    return key
