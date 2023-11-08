#!/usr/bin/python3
"""
Module 10-square

Contains the parent class BaseGeometry
with public instance method area and integer_validation

Contains subclass Rectangle
with instantiation of prv attributes width and height, validd by parent,
extends parents area method and prints with __str__

Contains subclass Square
with instantiation of prv attribute size, validated by superclass
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    inherits from Rectangle, who inherits from BaseGeometry
    methods:
        __init__(self, size)
    """
    def __init__(self, size):
        """
        initializes size
        Args:
            size (int): private
        """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
