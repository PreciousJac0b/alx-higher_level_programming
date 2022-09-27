#!/usr/bin/python3

"""Pascals triangle"""


def pascal_triangle(n):
    """
    Returns an array representation of the pascal's triangle
    """
    if n <= 0:
        return []
    pascal = [[1]]
    new_arr = pascal[-1]
    for i in range(n - 1):
        new_arr = pascal[-1]
        new = [1]
        for j in range(len(new_arr) - 1):
            new.append(new_arr[i] + new_arr[i+1])
        new.append(1)
        pascal.append(new)
    return pascal
