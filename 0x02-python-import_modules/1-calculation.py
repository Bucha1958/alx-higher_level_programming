#!/usr/bin/python3
# Importing specific functions from calculator_1.py
from calculator_1 import add, sub, mul, div

# Defining variables a and b
a = 10
b = 5

# Performing calculations and printing the results
result_add = add(a, b)
result_subtract = sub(a, b)
result_multiply = mul(a, b)
result_divide = div(a, b)

# Printing the results
print(f"{a} + {b} = {result_add}")
print(f"{a} - {b} = {result_subtract}")
print(f"{a} * {b} = {result_multiply}")
print(f"{a} / {b} = {result_divide}")
