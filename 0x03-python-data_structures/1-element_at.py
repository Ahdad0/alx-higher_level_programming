#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list) - 1:
        return None
    else:
        for index, value in enumerate(my_list):
            if index == idx:
                return value
