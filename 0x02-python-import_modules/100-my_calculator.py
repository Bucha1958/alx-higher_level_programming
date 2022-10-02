#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    length = len(argv) - 1
    operations = {"+": add, "-": sub, "*": mul, "/": div}
    if (length < 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    if (operator not in operations):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if (operator == "+"):
            print("{} + {} = {}".format(a, b, add(a, b)))
        if (operator == "-"):
            print("{} - {} = {}".format(a, b, sub(a, b)))
        if (operator == "*"):
            print("{} * {} = {}".format(a, b, mul(a, b)))
        if (operator == "/"):
            print("{} / {} = {}".format(a, b, div(a, b)))

