#!/usr/bin/python3
"""prints a matrix of integers
"""
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        b = 1
        for j in i:
            if (b != len(i)):
                print("{:d} ".format(j), end="")
            else:
                print("{:d}".format(j), end="")
            b = b+1
        print()
