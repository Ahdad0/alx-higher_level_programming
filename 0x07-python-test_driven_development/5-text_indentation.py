#!/usr/bin/python3

"""
    function text_indentation prints a text with 2 new
    lines after each of these characters: ., ? and : and
    handle errors
"""


def text_indentation(text):
    """
        print a text with 2 new lines after
        each of these characters: ., ? and :
    """
    count = 0

    if type(text) is not str:
        raise TypeError('text must be a string')

    for ch in text:
        if count == 1:
            count = 0
            if ch == ' ':
                continue
        if ch == '.' or ch == '?' or ch == ':':
            print(ch)
            print()
            count = 1
        else:
            print(ch, end="")
