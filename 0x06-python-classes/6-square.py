#!/usr/bin/python3
"""
    Importation of module is not allowed
"""


class Square:
    """
        Class Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
            Instantiation with optional size and optional position
        """

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
            Property getter for size
        """

        return self.__size ** 2

    @size.setter
    def size(self, value):
        """
            Property setter for size
        """

        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
            Property getter for position
        """
        
        return self.__position

    @position.setter
    def position(self, value):
        """
            Property setter for position
        """
        self.__position = value

        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        try:
            assert value[0] > 0 and value[1] > 0
        except Exception as TypeError:
            print("position must be a tuple of 2 positive integers")
        try:
            assert value[0] == int and value[1] == int
        except Exception as TypeError:
            print("position must be a tuple of 2 positive integers")


    def area(self):
        """
            Public instance method that returns the current square area
        """

        return self.__size * self.__size

    def my_print(self):
        """
            Public instance method that prints in stdout the square with the character #
        """

        if self.__size == 0:
            print()
        for i in range(self.position[1]):
            print("\n")
        for i in range(self.size):
            for count in range(self.size):
                print("#", end="")
            for count in range(self.position[0]):
                print(" ", end="")
            print()
