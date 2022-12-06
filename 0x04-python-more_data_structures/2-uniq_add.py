#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    sum_total = 0
    for count in new_list:
        sum_total += count
    return sum_total
