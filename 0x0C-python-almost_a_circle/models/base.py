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

    @staticmethod
    def from_json_string(json_string):
        """
            The method converts the JSON string to python object like dictionary
        """
        if json_string is None:
            return '[]'
        else:
            return (json.loads(json_string))

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

    @classmethod
    def create(cls, **dictionary):
        """
            This function create a dummy instance and assign attributes to it and return it
        """
        from models.rectangle import Rectangle
        from models.square import Square
        
        if cls.__name__ == "Square":
            new_create = cls(2)
        elif cls.__name__ == "Rectangle":
            new_create = cls(1, 3)
        new_create.update(**dictionary)
        return new_create

    @classmethod
    def load_from_file(cls):
        """
            This method checks for a json file, if it does exist it loads json string and convert them to list of instances and return it
        """
        file = cls.__name__ + ".json"
        
        try:
            with open(file, mode="r") as my_file:
                contents = cls.from_json_string(my_file.read())
        except:
            return []
        
        instances = []
        
        for content in contents:
            tmp = cls.create(**content)
        instances.append(tmp)
        return instances

