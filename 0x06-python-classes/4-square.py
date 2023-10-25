#!/usr/bin/python3
class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """__init__

        Args:
            size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif isinstance(size, int):
            self.__size = size

    def area(self):
        """square: return square"""
        return self.__size * self.__size

    @property
    def size(self):
        """respresent size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size

        Args:
            value (int): size of new value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        elif isinstance(value, int):
            self.__size = value
