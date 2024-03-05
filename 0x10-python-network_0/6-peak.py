#!/usr/bin/python3
"""define a function"""


def find_peak(list_of_integers):
    """find the peak in the list"""
    lenght = len(list_of_integers)
    if lenght == 0:
        return None
    big = max(list_of_integers)
    return big
