#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.items())
    convert_back_to_dict = dict(sorted_dict)
    return convert_back_to_dict
