#!/usr/bin/python3

"""Represents a rectangle class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A square class that inherits from a rectangle
    """
    def __init__(self, size):
        """Initializes the size variable of a square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Prints the rectangle class"""
        return "[Square] {}/{}".format(self.__size, self.__size)
