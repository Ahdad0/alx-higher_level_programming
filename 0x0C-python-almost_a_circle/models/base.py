#!/usr/bin/python3
"""
Module contains a class Base

Contains: private class __nb_objects, and class constructor __init__
Returns : JSON string representation of list dictionaries
Saves   : JSON strings of instance dictionaries into file
"""
import json


class Base:
    """
    defines a class Base
    Class Attributes:
        __nb_objects
    Methods:
        __init__(self, id=None)
    Static Methods:
    to_json_string(list_dictionaries)   from_json_string(json_string)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """assign"""
        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns JSON str representation of list dict"""
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)
