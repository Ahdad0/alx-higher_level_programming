#!/usr/bin/python3
def islower(c):
    s = ord(c)
    if s < 123 and s > 96:
        return True
    return False
