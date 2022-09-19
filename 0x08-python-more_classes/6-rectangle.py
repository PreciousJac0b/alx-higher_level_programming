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
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/sets the width of the rectangle"""
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
        """Get/sets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """computes and returns the area of the class"""
        return self.__width * self.__height

    def perimeter(self):
        """Computes and returns the perimeter of the class"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """Prints out the rectangle class using the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            if i != self.__height - 1:
                print()
        return ""

    def __repr__(self):
        """Returns an executable string of the class object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Executes when an instance of the class is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
