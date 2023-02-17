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
        if len(list_dictionaries) == 0:
            return ([])
        else:
            return (json.dumps(list_dictionaries))
