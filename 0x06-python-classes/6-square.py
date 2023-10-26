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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(position[0], int) and isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
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
        elif isinstance(value, int):
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
        if not isinstance(value[0], int) and isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        print to stdout
        square with the character #
        """
        resu = self.__size
        ano = self.__position[0]
        anoo = self.__position[1]
        if (resu == 0):
            print()
        else:
            for i in range(resu):
                for j in range(ano):
                    if not anoo > 0:
                        print(' ', end="")
                for x in range(resu):
                    print('#', end="")
                print()
