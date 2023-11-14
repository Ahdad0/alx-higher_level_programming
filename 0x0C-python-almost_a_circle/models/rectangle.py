#!/usr/bin/python3
"""
Module contains a class Rectangle

Inherits : from Base;
Inits    : superclass' id
Contains : private width, height, x, y
Contains : public method area
Prints   : [Rectangle] (<id>) <x>/<y> - <width>/<height
Updates  : attributes: arg1=id, arg2=width, arg3=height, arg4=x, arg5=y
"""


from models.base import Base


class Rectangle(Base):
    """
    defines a class Rectangle; inherits from class Base
    Inherited Attributes:
        id
    Class Attributes:
        __width          __height
        __x              __y
    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
        update(self, *args)
        width(self)      width(self, value)
        height(self)     height(self, value)
        x(self)          x(self, value)
        y(self)          y(self, value)
        area(self)       display(self)
        __str__(self)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Init"""
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """setter x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """setter y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area"""
        return self.__width * self.__height

    def display(self):
        """Print to stdout a rectangle using #'s"""
        for i in range(self.__y):
            print('\n', end='')
        for x in range(self.__height):
            for k in range(self.__x):
                print(' ', end='')
            for x in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """print to stdout"""
        return '[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
                self.__class__.__name__, self.id, self.__x, self.__y,
                self.__width, self.__height)

    def update(self, *args):
        """
        If args: set attributes in this order: id, width, height, x, y
        """
        if args:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.width = v
                elif i == 2:
                    self.height = v
                elif i == 3:
                    self.x = v
                elif i == 4:
                    self.y = v
