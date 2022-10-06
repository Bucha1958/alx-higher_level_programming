#!/usr/bin/python3
def element_at(my_list, idx):
    value = len(my_list)
    for i in my_list:
        if (idx < 0):
            return None
        elif (idx > value - 1):
            return None
        else:
            return my_list[idx]
