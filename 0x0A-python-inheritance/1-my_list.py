#!/usr/bin/python3
"""
Module 1-my_list

Contains a class MyList inherits from list
has public instance method to print sorted
"""


class MyList(list):
    """inherits from list

    methods:
        print_sorted(self)
    """
    def print_sorted(self):
        """prints a list of ints all sorted in the ascending order"""
        print(sorted(self))
