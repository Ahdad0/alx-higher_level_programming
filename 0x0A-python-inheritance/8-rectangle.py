#!/usr/bin/python3
"""
BaseGeometry class
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


"""
Rectangle class
"""


class Rectangle(BaseGeometry):
    """
    Methods
    """
    def __init__(self, width, height):
        """check and instantiation"""
        super().integer_validator(width, height)
        self.__width = width
        self.__height = height
