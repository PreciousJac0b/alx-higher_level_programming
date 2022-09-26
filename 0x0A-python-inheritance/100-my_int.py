#!/usr/bin/python3

"""Represents a rebel int class"""


class MyInt(int):
    """Rebel int class"""
    def __eq__(self, value):
        """Inverts the == operator"""
        return self.real != value

    def __ne__(self, value):
        """Inverts the != operator"""
        return self.real == value
