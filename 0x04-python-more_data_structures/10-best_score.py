#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary):
        new_sorted_list = sorted(a_dictionary.items(), key = lambda x: x[1]) 
        last_value = new_sorted_list[-1]
        final_value = last_value[0]
        return final_value
    else:
        return None
