#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.items(), key= lambda x: x[0])
    for key, value in sorted_dict:
        print("{}: {}".format(key, value))
