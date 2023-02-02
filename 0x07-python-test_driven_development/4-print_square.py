#!/usr/bin/python3
"""
    Module not allowed
"""


def print_square(size):
    i = 0
    hashes = "#"
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if (size is float) and (size < 0):
        raise TypeError("size must be an integer")
    while i < size:
        for count in range(size):
            print("{}".format(hashes), end="")
        print()
        i += 1
