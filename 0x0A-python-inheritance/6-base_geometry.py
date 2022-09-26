#!/usr/bin/python3

"""Represents BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class with an area method"""
    def area(self):
        """Raises an exception because the area
        is not implemented"""
        raise Exception("area() is not implemented")
