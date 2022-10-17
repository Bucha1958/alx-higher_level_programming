#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    new_list = []
    index = my_list[idx]
    if (idx < 0):
        return my_list
    elif (idx > length - 1):
        return my_list
    new_list = my_list
    new_list.remove(index)
    return new_list

