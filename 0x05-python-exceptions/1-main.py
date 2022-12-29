#!/usr/bin/python3
safe_print_list = __import__('00-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("number: {}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("number: {}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 3)
print("number: {}".format(nb_print))

