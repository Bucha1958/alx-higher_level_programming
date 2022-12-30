#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for elem in range(list_length):
        try:
            new_list.append(my_list_1[elem] / my_list_2[elem])
        except (ZeroDivisionError, TypeError, IndexError) as err:
            if (isinstance(err, ZeroDivisionError)):
                print("division by 0")
            elif (isinstance(err, TypeError)):
                print("wrong type")
            elif (isinstance(err, IndexError)):
                print("out of range")
            new_list.append(0)
        finally:
            pass
    return new_list
        
