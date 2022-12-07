#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_key = a_dictionary.keys()
    dict_values = a_dictionary.values()
    new_list = [i * 2 for i in dict_values]
    new_dict = {}
    for key in dict_key:
        for value in new_list:
            new_dict[key] = value
            new_list.remove(value)
            break
    return new_dict
