#!/usr/bin/python3
"""
Contains funct that
returns: dictionary description with simple data structure
(list, dictionary, dictionary, string)
for JSON serialization of an obj
"""


def class_to_json(obj):
    """Returns dictionary description with simple data structure

    Args:
        obj: python obj
    """
    return obj.__dict__
