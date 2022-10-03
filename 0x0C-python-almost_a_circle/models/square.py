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
                                             self.id, self.x, self.y,
                                             self.width)

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

    def update(self, *args, **kwargs):
        """Updates class instances"""
        j = 0
        if args and len(args) != 0:
            for elem in args:
                if j == 0:
                    self.id = elem
                elif j == 1:
                    self.size = elem
                elif j == 2:
                    self.x = elem
                elif j == 3:
                    self.y = elem
                j += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'size':
                    self.size = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v

    def to_dictionary(self):
        """
        Returns dictionary representation of
        the class instance
        """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
