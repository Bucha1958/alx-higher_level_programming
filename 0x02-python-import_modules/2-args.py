#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    size = len(argv)
    if (size == 1):
        print("{:d} {}.".format(0, "arguments"))
    elif (size == 2):
        print("{:d} {}:".format(1, "argument"))
        for i in range(1, size):
            print("{:d}: {}".format(size - 1, argv[i]))
    else:
        print("{:d} {}:".format(size - 1, "arguments"))
        for i in range(1, size):
            print("{:d}: {}".format(i, argv[i]))
