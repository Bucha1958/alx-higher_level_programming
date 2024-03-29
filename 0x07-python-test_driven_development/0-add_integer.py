#!/usr/bin/python3
"""
    Importation of module are not allowed
"""

def add_integer(a, b=98):
    """
        Function that adds two parameters passed to it
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a + b)
