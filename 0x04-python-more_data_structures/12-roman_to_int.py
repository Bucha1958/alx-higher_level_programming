#!/usr/bin/python3
def value(r):
    if r == "I":
        return (1)
    if r == "V":
        return (5)
    if r == "X":
        return (10)
    if r == "L":
        return (50)
    if r == "C":
        return (100)
    if r == "D":
        return (500)
    if r == "M":
        return (1000)
    return -1

def roman_to_int(roman_string):
    result = 0
    i = 0
    if (roman_string and isinstance(roman_string, str)):
        while i < (len(roman_string)):
            symbol_1 = value(roman_string[i])
            if (i + 1 < len(roman_string)):
                symbol_2 = value(roman_string[i + 1])
                if (symbol_1 >= symbol_2):
                    result += symbol_1
                    i = i + 1
                else:
                    result = symbol_2 - symbol_1
                    i = i + 2
            else:
                result = result + symbol_1
                i = i + 1
        return result
    else:
        return (0)
