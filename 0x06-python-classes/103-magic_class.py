#!/usr/bin/python3

"""Defines a Magic Circle Class"""

import math


class MagicClass:
    def __init__(self, radius=0):
        """Initializes MagicClass

            Args:
                radius(int or float): Radius of MagicClass
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius is not a number")
        self.__radius = radius

    def area(self):
        """Returns area of circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Returns circumference of circle"""
        return 2 * math.pi * self.__radius
