#!/usr/bin/python3

"""Represents a rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from the basegeometry class"""
    def __init__(self, width, height):
        """
        Validates and initializes the width and height attributes
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """Computes the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """prints a string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
