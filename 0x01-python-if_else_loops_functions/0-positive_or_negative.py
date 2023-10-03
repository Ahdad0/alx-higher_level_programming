#!/usr/bin/python3
import random
number = random.randint(-10, 10)
match number:
    case n if n > 0:
        print(f"{number} is positive")
    case 0:
        print(f"{number} is zero")
    case n if n < 0:
        print(f"{number} is negative")
