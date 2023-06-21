#!/usr/bin/python3
import hidden_4


def print_defined_names():
    names = []
    for name in dir(hidden_4):
        if not name.startswith("__"):
            names.append(name)

    for name in sorted(names):
        print(name)


print_defined_names()
