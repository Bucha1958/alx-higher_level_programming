#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    value = new_list.index(search)
    new_list[value] = replace
    return new_list
