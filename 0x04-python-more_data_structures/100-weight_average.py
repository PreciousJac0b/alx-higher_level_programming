#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_score = 0
    sum_weight = 0
    for s, w in my_list:
        sum_score += (s * w)
        sum_weight += w
    return sum_score / sum_weight
