#!/usr/bin/python3
"""
    You are not allowed to import any module
"""


class Square():
    """
        Define a class with a private attribute
    """
    def __init__(self, size=0):
        """
            Private instance attribute
        """
        self.__size = size
        try:
            assert type(size) == int
        except TypeError:
            print("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
