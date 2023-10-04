#!/usr/bin/python3
def remove_char_at(str, n):
    c = ""
    for i, u in enumerate(str):
        if (i != n):
            c += u
    return c
