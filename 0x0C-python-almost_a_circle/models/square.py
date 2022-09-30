#!/usr/bin/python3

"""
Represents a Square class
that inherits fr0m the 
Rectangle class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Displays the square class"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size field getter"""
        return self.width

    @size.setter
    def size(self, value):
        """The size attribute decorator setter method"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = self.height = value
