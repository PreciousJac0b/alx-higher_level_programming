#!/usr/bin/python3

"""Represents a Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square that inherits methods from
    a rectangle class
    """
    def __init__(self, size):
        """Initializes the square class"""
        self.__size = self.integer_validator("size", size)

    def area(self):
        """Computes the area of the square class"""
        return self.__size ** 2

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
