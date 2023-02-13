#!/usr/bin/python3
"""
Module not imported in this script
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
        
