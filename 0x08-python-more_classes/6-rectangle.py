#!/usr/bin/python3

""" Rectangle Class"""


class Rectangle:
    """
         Defines class rectangle with private attribute width and height

        Args:
            width (int): width
            height (int): height

        Functions:
            __init__(self, width, height)
            width(self)
            width(self, value)
            height(self)
            height(self, value)
            __str__(self)
            area(self)
            perimeter(self)
            __repr__(self)
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initialize rectangles """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    def __str__(self):
        """print the rectangle with the character #"""
        result = ''
        if self.width == 0 or self.height == 0:
            return ''
        for j in range(self.height):
            for i in range(self.width):
                result += '#'
            result += '\n'
        return result[:-1]

    def __repr__(self):
        """ return a string representation of the rectangle """
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """print ... when an instance of Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @property
    def width(self):
        """ Getter returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter sets width if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter sets height if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            result = 0
        else:
            result = (self.width + self.height) * 2
        return result
