#!/usr/bin/python3
"""
Module contains a class Square

Inherits : from Rectangle;
Inits    : superclass' id, width (as size), height (as size), x, y
Contains : public attribute size
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    defines a class Square; inherits from class Rectangle
    Inherited Attributes:
        id
        __weight        __height
        __x             __y
    Class Attributes:
        size
    Inherted Methods:
        width(self)      width(self, value)
        height(self)     height(self, value)
        x(self)          x(self, value)
        y(self)          y(self, value)
    Methods:
        __str__
        __init__(self, size, x=0, y=0, id=None)
        size(self)       size(self, value)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """init"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter size - sets width and height as size"""
        self.width = value
        self.height = value

    def __str__(self):
        """print to stdout"""
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
                self.id, self.x, self.y, self.size)
