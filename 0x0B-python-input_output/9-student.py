#!/usr/bin/python3

"""
Represents a student class
"""


class Student:
    """Represents a Student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary representation"""
        return self.__dict__
