#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5

    print("{:d} + {:d} = {:d}".format(a, b, a + b))
    print("{:d} - {:d} = {:d}".format(a, b, a - b))
    print("{:d} * {:d} = {:d}".format(a, b, a * b))
    print("{:d} / {:d} = {:d}".format(a, b, a / b))
