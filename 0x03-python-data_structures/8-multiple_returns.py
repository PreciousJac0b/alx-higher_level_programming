#!/usr/bin/python3


def multiple_returns(sentence):
    if not sentence:
        first = None
    else:
        first = sentence[:1]
    length = len(sentence)
    return (length, first)
