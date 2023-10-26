#!/usr/bin/python3

"""Class of square"""


class Square:
    """Represent a square"""
    def __init__(self, size=0, position=(0, 0)):
        """__init__

        Args:
            size (int): size of square
            position (int): position of spaces
        """
        self.__size = size
        self.__position = position

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
            value (int): size of new
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """acces to position"""
        return self.__position

    @position.setter
    def position(self, value):
        """position

        Args:
            value (int): set a new value
        """
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        print to stdout
        square with the character #
        """
        if (self.size == 0):
            print()
            return

        print("\n" * self.position[1], end="")

        for i in range(self.size):
            for j in range(self.position[0]):
                print(' ', end="")
            for x in range(self.size):
                print('#', end="")
            print()
