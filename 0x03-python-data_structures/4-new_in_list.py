#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = my_list[:]
    if idx < 0:
        return copy_list
    elif idx > len(copy_list) - 1:
        return copy_list
    else:
        for index, value in enumerate(copy_list):
            if index == idx:
                copy_list[index] = element
                return copy_list
