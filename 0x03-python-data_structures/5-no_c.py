#!/usr/bin/python3
def no_c(my_string):

    new_string = ""

    for cha in my_string:
        if cha != 'c' and cha != 'C':
            new_string += cha

    return new_string
