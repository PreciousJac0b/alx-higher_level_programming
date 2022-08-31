#!/usr/bin/python3


def uniq_add(my_list=[]):
    result = 0
    new_list = set(my_list)
    for elem in new_list:
        result += elem
    return result
