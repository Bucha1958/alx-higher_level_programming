#!/usr/bin/python3
from models.rectangle import Rectangle
"""
    This file will contain class Square that will inherit from class Rectangle
"""


class Square(Rectangle):
    """
        Class Square created
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            Init function called which must inherits from the super class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            Getter method
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """
            Setter method
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
            It prints the string representation of instance object
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
