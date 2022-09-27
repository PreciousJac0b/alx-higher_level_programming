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

    def to_json(self, attrs=None):
        """returns dictionary representation"""
        new_dict = self.__dict__
        new_dict2 = {}
        if type(attrs) == list:
            for elem in new_dict:
                if elem in attrs:
                    new_dict2[elem] = new_dict[elem]
            return new_dict2
        else:
            return new_dict
