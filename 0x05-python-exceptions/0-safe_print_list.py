#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len_of_list = 0
    number_of_elements = 0
    counter = 0

    for elem in my_list:
        len_of_list += 1
    try:
        if (x == 0):
            return number_of_elements
        elif (x >= len_of_list):
            for elem in my_list:
                print("{}".format(elem), end="")
            print()
            return len_of_list
        else:
            for elem in range(0, x):
                print("{}".format(my_list[elem]), end="")
                number_of_elements += 1
    except IndexError:
        pass
    print()
    return number_of_elements
