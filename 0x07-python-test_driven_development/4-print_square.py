#!/usr/bin/python3

"""
    function print_square : print size of square of '#'
    and raise exceptions if size is not an integer and
    if it is smaller than 0
"""


def print_square(size):
    """
        print size of square of '#'
    """
    if type(size) is float and size < 0 or type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('{:s}'.format('#'), end="")
        print()
