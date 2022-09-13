#!/usr/bin/python3

"""Contains a Square class"""


class Square:
    """Square class with optional size property
        Size must be an integer and must be greater
        than zero
    """
    def __init__(self, size=0):
        """Initializes a new square


        Args:
            size (int): The size of a new square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
