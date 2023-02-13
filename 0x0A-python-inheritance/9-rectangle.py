#!/usr/bin/python3
"""
No module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class rectangle created
    """

    def __init__(self, width, height):
        """
        Instantiation initialized
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Method must be implemented
        """
        return self.width * self.height

    def __str__(self):
        """
        It prints out the string of the object passed to it
        """
        return ("[{}] {}/{}".format(type(self).__name__,self.width, self.height))
