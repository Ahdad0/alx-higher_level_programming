#!/usr/bin/python3
"""
Base class
"""


class Base:
    """
    Method:
        public class attribute: __nb_objects
        __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """assign"""
        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
