#!/usr/bin/python3
"""
Module contains a class Base

Contains: private class __nb_objects, and class constructor __init__
Returns : JSON string representation of list dictionaries
Saves   : JSON strings of instance dictionaries into file
Returns : Python obj of JSON string representation
Returns : instance with attributes already set
Returns : list of instances
Saves   : to CSV and loads from CSV file
"""


import json


class Base():
    """
    defines a class Base
    Class Attributes:
        __nb_objects
    Methods:
        __init__(self, id=None)
    Static Methods:
        to_json_string(list_dictionaries)   from_json_string(json_string)
    Class Methods:
        save_to_file(cls, list_objs)        save_to_file_csv(cls, list_objs)
        load_from_file(cls)                 load_from_file_csv(cls)
        create(cls, **dictionary)           draw(list_rectangles, list_squares)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Init id, increment class attribute if no id and set as id"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON str representation of list dict"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns Python obj of JSON str representation"""
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

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

    @classmethod
    def create(cls, **dictionary):
        """Returns a instance with attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filenamee = cls.__name__ + ".json"
        k = []
        try:
            with open(filenamee, "r") as f:
                instances = cls.from_json_string(f.read())
            for i, dic in enumerate(instances):
                k.append(cls.create(**instances[i]))
        except Exception:
            pass
        return k
