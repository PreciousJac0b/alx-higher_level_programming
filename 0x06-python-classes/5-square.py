#!/usr/bin/python3

"""Defines a Square class"""


class Square:
    """ Represents a Square"""
    def __init__(self, size=0):
        """
        Initializes a new square

        Args:
            size (int): The size of a new square
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """Prints a square"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
