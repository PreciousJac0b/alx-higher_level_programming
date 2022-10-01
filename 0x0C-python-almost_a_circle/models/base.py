#!/usr/bin/python3
"""
Represents a base class
"""

import json


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
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts object to json string"""
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes json object of list_objs to class name.js0n
        """
        filename = "{}.json".format(cls.__name__)
        new_list = []
        with open(filename, 'w', encoding='utf-8') as f:
            if not list_objs:
                json.dump([], f)
            else:
                for elem in list_objs:
                    new_list.append(elem.to_dictionary())
                f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list representation of
        json_string object
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy_instance = cls(1, 2, 3, 4, 5)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Class method to load instance fr0m json file
        """
        filename = '{}.json'.format(cls.__name__)
        if not os.path.exists(filename):
            return []
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        parsed = cls.from_json_string(content)

        load_list = []
        for elem in parsed:
            load_list.append(cls.create(**elem))
        return load_list
