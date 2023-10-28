#!/usr/bin/python3

"""
    function ``add_integer`` that addition a and b
    and return the result, if parameters are not int or float
    raise TypeError and you must casted a and b if they are float
"""


def add_integer(a, b=98):
    """
        return addition of a + b
    """
    if not (type(a) is int or type(a) is float):
        raise TypeError('a must be an integer')
    if not (type(b) is int or type(b) is float):
        raise TypeError('b must be an integer')

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
