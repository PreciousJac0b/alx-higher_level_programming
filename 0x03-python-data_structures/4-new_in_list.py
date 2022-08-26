#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if not my_list:
        return
    elif idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    copied = my_list.copy()
    copied[idx] = element
    return copied
