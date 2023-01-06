#!/usr/bin/python3
"""
    Importation of module is not allowed
"""


class Square():
    """
        definition of class Square
    """
    def __init__(self, size=0):
        """
            instantiation
        """
        self.__size = size

    @property
    def size(self):
        """
            Method gets the value of the class
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            Setter method sets the value of the object
        """
        self.__size = value
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise TypeError("size must be >= 0")

    def area(self):
        """
            Public instance method
        """
        return self.__size ** 2

    def my_print(self):
        """
            Public instance method that prints in stdout the square with the character #
        """
        if (self.__size):
            for count in range(self.__size):
                print("#" * self.__size, end='')
                print()
        else:
            print()
