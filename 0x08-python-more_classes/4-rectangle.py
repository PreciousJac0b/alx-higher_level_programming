#!/usr/bin/python3

"""
Contains a printable rectangle class with
methods area and perimeter.

"""


class Rectangle:
    """
    Imitates a real rectangle
    Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
    Raises:
        TypeError: if either height or width isn't an integer
        ValueError: if either height or width isn't greater than 0
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            if i != self.__height - 1:
                print()
        return ""

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
