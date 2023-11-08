#!/usr/bin/python3
"""
contains methode is_kind_of_class
return true if obj is an istance or object
otherwize false
"""


def is_kind_of_class(obj, a_class):
    """
    isinstynce() to get class and any parent classes to

    Return:
        True if obj is a an instance of, or if the object
        is an instance of a class that inherited from
        otherwize return False
    """
    return isinstance(obj, a_class)
