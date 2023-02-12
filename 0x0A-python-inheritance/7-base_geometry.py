#!/usr/bin/python3
"""
No importation of module
"""


class BaseGeometry():
    """
    BaseGeometry class created
    """

    def area(self):
        """
        public instance method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        public instance method
        """
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value < 0:
            raise ValueError(name+" must be greater than 0")
