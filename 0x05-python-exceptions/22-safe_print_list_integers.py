#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    len_list = 0
    number_of_elements = 0
    for elem in my_list:
        len_list += 1
    try:
        if (x == 0):
            return number_of_elements
        elif (x == len_list):
            for elem in my_list:
                number_of_elements += 1
                if (type(elem) != int):
                    continue
                print("{:d}".format(elem), end="")
            print()
        elif (x < len_list):
            for elem in range(0, x):
                number_of_elements += 1
                if (type(elem) != int):
                    continue
                print("{}".format(my_list[elem]), end="")
            print()
    except IndexError:
        pass
    return number_of_elements
