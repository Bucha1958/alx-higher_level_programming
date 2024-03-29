#!/usr/bin/python3
"""
No importation of module
"""


class Rectangle():
    """
    Class rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialization
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """
        Getter
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        setter
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise TypeError("height must >= 0")

        self.__height = value
        

    
