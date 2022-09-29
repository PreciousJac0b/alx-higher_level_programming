#!/usr/bin/python3

"""
A Rectangle class that inherits from the Base Class
"""

from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle
    Inherited all fields from base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the rectangle class

        Args:
            width (int): The width of the rectangle class
            height (int): The height of the rectangle class
            x (int): x
            y (int): y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Field width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Field width setter with input validations"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Field height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Field height setter with input validation"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Field x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Field x setter with input validations"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Field y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Field y setter with input validations"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
