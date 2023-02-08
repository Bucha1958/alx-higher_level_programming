#!/usr/bin/python3
"""
No module for this script
"""



class Square():
    """
    Square class
    """

    def __init__(self, size):
        """
        Instantiation
        """

        self.__size = size

    @property
    def size(self):
        """
        property getter
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        property setter
        """

        if not isinstance(value, int):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        public instance method that returns the current square area
        """

        return self.__size * self.__size

    def __le__(self, other):
        """
        less than equal to
        """

        return self.area() <= other.area()

    def __lt__(self, other):
        """
        less than
        """

        return self.area() < other.area()

    def __eq__(self, other):
        """
        equal to
        """

        return self.area() == other.area()

    def __gt__(self, other):
        """
        greater than
        """

        return self.area() > other.area()

    def __ge__(self, other):
        """
        greater equal to
        """

        return self.area() >= other.area()

    def __ne__(self, other):
        """
        not equal to
        """

        return self.area() != other.area()
