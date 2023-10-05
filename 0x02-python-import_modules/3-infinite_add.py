#!/usr/bin/python3
import sys

o = 0
result = 0

if __name__ == "__main__":
    for i in sys.argv:
        if (o != 0):
            result += int(i)
        o += 1
    print("{:d}".format(result))
