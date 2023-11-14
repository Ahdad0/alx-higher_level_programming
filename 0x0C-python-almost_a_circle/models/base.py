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
        from_json_string(json_string)
    Class Methods:
        save_to_file(cls, list_objs)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """assign"""
        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON str representation of list dict"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save json str of all instances into file"""
        objs = []
        if list_objs is not None:
            for o in list_objs:
                objs.append(cls.to_dictionary(o))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """Returns Python obj of JSON str representation"""
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)
