#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
nb_keys = print_sorted_dictionary(a_dictionary)
print("Number of keys: {}".format(nb_keys))



