#!/usr/bin/python3

def max_integer(my_list=[]):
    length = len(my_list)
    organise = sorted(my_list)
    if (length == 0):
        return None
    else:
        last = organise[-1]
        return last
