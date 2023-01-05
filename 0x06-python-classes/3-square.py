#!/usr/bin/python3
"""
    Importing of module is not allowed
"""


class Square():
    """
        Class that defines a square
    """
    def __init__(self, size=0):
        """
            Instantiation
        """
        self.__size = size
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
   
    def area(self):
        """
            Public instance method
        """
        return self.__size ** 2
