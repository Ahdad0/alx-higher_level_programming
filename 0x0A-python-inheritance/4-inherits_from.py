#!/usr/bin/python3
"""
contains the methode inherits_from
return true if obj is instance otherwize
false
"""


def inherits_from(obj, a_class):
    """
    use issubclass() to get what object is a subclass of

    Return:
        True if obj is instance of class that it inherits from
        the specified class, otherwise False
    """
    return (type(obj) != a_class and issubclass(type(obj), a_class))
