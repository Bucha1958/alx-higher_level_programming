#!/usr/bin/python3

new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 6]
idx = 4
element = 9

new_list = new_in_list(my_list, idx, element)
print(my_list)
print(new_list)
