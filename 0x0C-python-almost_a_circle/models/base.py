#!/usr/bin/python3
"""
    This file will contain the base class of all other classes in this project
"""

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
