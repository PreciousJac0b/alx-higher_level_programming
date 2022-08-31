#!/usr/bin/python3


def roman_to_int(roman_string):
    rod = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_number = 0
    if len(roman_string) == 1:
        return decimal_number + rod[roman_string[0]]
    for i in range(len(roman_string) - 2):
        if rod[roman_string[i]] >= rod[roman_string[i + 1]]:
            decimal_number += rod[roman_string[i]]
        else:
            first = rod[roman_string[i]]
            decimal_number += abs(first - rod[roman_string[i + 1]])
            i += 1
    if rod[roman_string[-2]] < rod[roman_string[-1]]:
        decimal_number += abs(rod[roman_string[-2]] - rod[roman_string[-1]])
    else:
        decimal_number += rod[roman_string[-2]] + rod[roman_string[-1]]
    return decimal_number
