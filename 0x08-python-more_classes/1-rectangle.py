#!/usr/bin/python3

"""define a rectangle class"""


class Rectangle:
    """defines a rectangle with private attribute

    Args:
        width (int): specify the width
        height (int): specify the height

    functions:

    __init__(self, width=0, height=0)
    width(self)
    width(self, value)
    height(self)
    height(self, value)
    """

    def __init__(self, width=0, height=0):
        """ initiliaze rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter set width """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """ getter returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter set height """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')

        self.__height = value
