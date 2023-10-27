#!/usr/bin/python3

def add_integer(a, b=98):
    """addition of two integer
    and raise TypeError if parametres
    are not either int or float

    Args:
        a (int, float): integer or float
        b (int, float): integer or value

    Return:
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
