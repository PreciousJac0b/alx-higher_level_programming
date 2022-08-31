#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    sort_dicts = sorted(a_dictionary.items())
    for k, v in sort_dicts:
        print("{}: {}".format(k, v))
