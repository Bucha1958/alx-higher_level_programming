#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if (length == 0):
        return (length, None)
    else:
        new_tuple = (length, first)
        return new_tuple
