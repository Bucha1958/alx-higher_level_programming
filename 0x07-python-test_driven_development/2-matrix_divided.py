#!/usr/bin/python3
"""
    Don't import a new model
"""

def matrix_divided(matrix, div):
    """
        Divide each element in the matrix
    """
    new_matrix = []
    int_err = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError(int_err)
    
    for row in matrix:
        new_row = []
        if not isinstance(row, list):
            raise TypeError(int_err)
        if (len(matrix[0]) is not len(row)):
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(int_err)
            result = round(elem / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)
    return new_matrix
