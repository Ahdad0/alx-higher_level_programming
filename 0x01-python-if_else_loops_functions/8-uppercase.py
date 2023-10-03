#!/usr/bin/python3
def uppercase(str):
    for i in str:
        n = 0
        if i <= 'z' and i >= 'a':
            n = 32
        print(("{:c}".format(ord(i)-n)), end='')
    print()
