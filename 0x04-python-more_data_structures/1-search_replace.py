#!/usr/bin/python3


def search_and_replace(x, search, replace):
    if x == search:
        return replace
    return x


def search_replace(my_list, search, replace):
    return list(map(lambda x: search_and_replace(x, search, replace), my_list))
