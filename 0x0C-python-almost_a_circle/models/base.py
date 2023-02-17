#!/usr/bin/python3
"""
    This file will contain the base class of all other classes in this project
"""
import json


class Base():
    """
        Base class created
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Instantiation initialized
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Method that returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return '[]'
        else:
            return (json.dumps(list_dictionaries, indent=4))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        classmethod writes json object list into the file.
        """
        if list_objs is None:
            with open(cls.__name__ + ".json", mode="w") as my_file:
                my_file.write('[]')
        else:
            with open(cls.__name__ + ".json", mode="w") as my_file:
                my_file.write(cls.to_json_string([x.to_dictionary() for x in list_objs]))
                              
