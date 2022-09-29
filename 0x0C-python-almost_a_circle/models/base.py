#!/usr/bin/python3
"""
Represents a base class
"""


class Base:
    """
    Base class for subsequent files in this project
    Manages id attributes of all future classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the basee class with the id attribute
        if id is None, it sets the id attribute to the value
        of the __nb_objects private attribute

        Args:
            id: The identity of the new instance
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
