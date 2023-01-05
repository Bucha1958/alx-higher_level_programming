#!/usr/bin/python3
"""
    Importation of module is not allowed
"""


class Square():
    """
        Square name defines a class
    """
    def __init__(self, size=0):
        """
            Instantiation
        """
        self.__size = size

    @property
    def size(self):
        """
            Getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            Setter
        """
        self.__size = value
        try:
          assert type(value) == int
        except:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        """
            Public method
        """
        return self.__size ** 2
