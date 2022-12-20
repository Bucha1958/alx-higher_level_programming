#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    number_of_elements = 0
    if (my_list):
        for elem in range(0, x):
            try:
                print("{:d}".format(my_list[elem]), end="")
                number_of_elements += 1
            except (ValueError, TypeError):
                pass
        print()
        return number_of_elements
