#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    v = my_list[0]
    for i in range(1, len(my_list)):
        if (v < my_list[i]):
            v = my_list[i]
    return v
