#!/usr/bin/python3

"""
    function say_my_name print 'my name is followed by first_name
    and last name' and raise exception if it not a string
"""


def say_my_name(first_name, last_name=""):
    """
        print 'my name is {first_name} {last_name}'
    """
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = 'abcdefghijklmnopqrstuvwxyz' + upper

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')

    for first in first_name:
        count = 0
        for letter in letters:
            if letter == first:
                count = 1
        if count != 1:
            raise TypeError('first_name must be a string')
    if last_name:
        for last in last_name:
            count = 0
            for letter in letters:
                if letter == last:
                    count = 1
            if count != 1:
                raise TypeError('last_name must be a string')

    print('My name is {:s} {:s}'.format(first_name, last_name))
