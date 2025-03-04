#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if 10 >= number > 0:
    print(f" {number} :is Positive")
elif 0 > number >= -10:
    print(f"{number} :is Negative")
else:
    print(f"{number} :is Zero")
    