#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(number, "is positive",end="")
elif number == 0:
    print(number, "is zero",end="")
else:
    print(number, "is negative",end="")
