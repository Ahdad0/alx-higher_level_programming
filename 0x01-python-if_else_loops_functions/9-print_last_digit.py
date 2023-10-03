#!/usr/bin/python3

def print_last_digit(number):
    n = number
    if (n < 0):
        n *= -1

    print("{:d}".format(n % 10), end="")
    return n % 10
