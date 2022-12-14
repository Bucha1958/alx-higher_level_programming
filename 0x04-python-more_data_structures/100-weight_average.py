#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    denominator = 0
    if my_list == []:
        return 0
    for elem in my_list:
        total = total + elem[0] * elem[1]
        denominator = denominator + elem[1]
    return total / denominator
