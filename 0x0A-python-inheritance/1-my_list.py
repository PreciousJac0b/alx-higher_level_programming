#!/usr/bin/python3

"""A class that inherits from the list class"""


class MyList(list):
    """
    Inherits all method from the list class
    and adds new methods
    """
    def print_sorted(self):
        """Prints sorted list of type parent class"""
        new_list = sorted(self)
        print(new_list)
