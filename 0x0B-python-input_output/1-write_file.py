#!/usr/bin/python3
def write_file(filename="", text=""):
    """
        Function that writes a string to a text file and returns the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as my_file:
        my_file.write(text)
    return (len(text))
