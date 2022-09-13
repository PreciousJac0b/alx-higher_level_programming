#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """Represents a Square"""

    def __init__(self, size=0):
        """
        Initializes a Square class that validates
        the type and value of the parameter
        passed into it

        Args:
            size (int): The size of the new square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
