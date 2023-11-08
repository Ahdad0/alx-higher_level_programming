#!/usr/bin/python3
"""
Module 6-base_geometry
Contains empty class BaseGeometry with pub instance method area
"""


class BaseGeometry:
    """
    Methods:
        area()
        integer_validato()
    """
    def integer_validator(self, name, value):
        """check value"""
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')

    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")
