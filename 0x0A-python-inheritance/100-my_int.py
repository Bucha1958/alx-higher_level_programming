#!/usr/bin/python3
"""
No module should be imported
"""


class MyInt(int):
    def __init__(self, number):
        self.number = number

    def __eq__(self, val):
        return (self.number == val)

    def __ne__(self, val):
        return (self.number != val)

    def __str__(self):
        return (str(self.number))
