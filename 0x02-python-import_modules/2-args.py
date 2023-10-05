#!/usr/bin/python3
import sys

size = len(sys.argv) - 1
o = 0

if __name__ == "__main__":
    if (size != 1):
        print("{:d} arguments{}".format(size, '.' if size == 0 else ':'))
    else:
        print("{:d} argument:".format(size))
    for i in sys.argv:
        if (o != 0):
            print("{:d}: {}".format(o, i))
        o += 1
