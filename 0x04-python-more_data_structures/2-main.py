#!/usr/bin/python3
simple_delete = __import__('8-simple_delete').simple_delete
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'language': "C", 'number': 13, 'track': "Low level",'ids': [1, 2, 3]}
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")

new_dict = simple_delete(a_dictionary, 'number')
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)



