#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if -10 < number > 0:
    print(f" {number} :is negative")
elif 0 < number < 10:
    print(f"{number} :is Positive")
else:
    print(f"{number} :is Zero")
