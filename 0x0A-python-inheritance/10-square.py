#!/usr/bin/python3
"""
No importation of module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class created
    """

    def __init__(self, size):
        """
        Instantiation initialized
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.size ** 2
