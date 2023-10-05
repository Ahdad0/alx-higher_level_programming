#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

o, a, b = 0, 0, 0
ope = ""

arg = len(sys.argv) - 1

for i in sys.argv:
    if (o == 1):
        a = int(i)
    elif (o == 2):
        ope = i
    elif (o == 3):
        b = int(i)
    o += 1

if __name__ == "__main__":
    if arg is not 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    match ope:
        case "+":
            print("{} {} {} = {}".format(a, ope, b, add(a, b)))
        case "-":
            print("{} {} {} = {}".format(a, ope, b, sub(a, b)))
        case "*":
            print("{} {} {} = {}".format(a, ope, b, mul(a, b)))
        case "/":
            print("{} {} {} = {}".format(a, ope, b, div(a, b)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
