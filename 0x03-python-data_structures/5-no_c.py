#!/usr/bin/python3
"""
1. Count the number of characters in the string and store it in variable
2. convert the string to be in list format and store in a variable
3. Loop the count variable and use remove function to remove the character from the list
4. Repeat 1, 2, 3 process until you remove your desired characters
5. Use join function to convert the list to string

"""
def no_c(my_string):
    counts = my_string.count('c')
    new_string = list(my_string)
    while counts:
        new_string.remove('c')
        counts -= 1
    counts = my_string.count('C')
    while counts:
        new_string.remove('C')
        counts -= 1
    new_string = ''.join(new_string)
    return new_string
