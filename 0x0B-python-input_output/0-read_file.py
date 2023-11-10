#!/usr/bin/python3
"""
read and print contents from a file
"""


def read_file(filename=""):
    """read and print contents from a text"""
    with open("my_file_0.txt", "r", encoding="utf-8") as f:
        print(f.read(), end="")
