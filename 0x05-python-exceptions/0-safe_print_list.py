#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    o = 0
    try:
        for i in range(0, x):
            print(my_list[i], end="")
            o += 1
        print()
        return o
    except IndexError:
        print()
        return o
