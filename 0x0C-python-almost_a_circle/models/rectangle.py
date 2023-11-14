#!/usr/bin/python3
"""
Module contains a class Rectangle
inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """define a class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter width"""
        return self.__width

    @property
    def height(self):
        """getter height"""
        return self.__height

    @property
    def x(self):
        """getter x"""
        return self.__x

    @property
    def y(self):
        """getter y"""
        return self.__y

    @width.setter
    def width(self, value):
        """setter width"""
        self.__width = value

    @height.setter
    def height(self, value):
        """setter height"""
        self.__height = value

    @x.setter
    def x(self, value):
        """setter x"""
        self__x = value

    @y.setter
    def y(self, value):
        """setter y"""
        self.__y = value
