#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Function that returns True if the object is an instance of a class
    """
    if issubclass(type(obj), a_class):
        return True
    return (type(obj) != a_class)
