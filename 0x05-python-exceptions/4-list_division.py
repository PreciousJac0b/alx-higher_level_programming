#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for q, r in zip(my_list_1, my_list_2):
        try:
            value = q / r
        except ZeroDivisionError:
            value = 0
            print("division by 0")
        except TypeError:
            value = 0
            print("wrong type")
        finally:
            new_list.append(value)
    if len(my_list_1) != len(my_list_2):
        print("out of range")
        ranged = abs(len(my_list_1) - len(my_list_2))
        for i in range(ranged):
            new_list.append(0)
    if list_length > len(new_list):
        for i in range(list_length - len(new_list):
                new_list.append(0)
    return new_list
