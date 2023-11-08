#!/usr/bin/python3
"""
Rectangle class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Methods:
        area()
    """

    def __init__(self, width, height):
        """
        check and instantiation

        Args:
            width (int): private
            height (int): private
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """print rectangle foolowed width/height"""
        return f'[Rectangle] {self.__width}/{self.__height}'
