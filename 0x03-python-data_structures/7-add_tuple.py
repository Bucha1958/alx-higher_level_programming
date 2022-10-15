#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    first_length = len(tuple_a)
    second_length = len(tuple_b)
    if (first_length == 1):
        tuple_a = (tuple_a[0], 0)
    elif (second_length == 1):
        tuple_b = (tuple_b[0], 0)
    elif (first_length > 2):
        tuple_a = (tuple_a[0], tuple_a[1])
    elif (second_length > 2):
        tuple_b = (tuple_b[0], tuple_b[1])
    elif (first_length == 0):
        tuple_a = (0, 0)
    elif (second_length == 0):
        tuple_b = (0, 0)
    sum_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return sum_tuple


