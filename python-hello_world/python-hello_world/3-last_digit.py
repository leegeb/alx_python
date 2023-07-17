#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
prefix = "Last digit of {} is".format(number)

if number < 0:
    last_digit = -last_digit
    print("{} {} and is less than 6 and not 0".format(prefix, last_digit))
elif last_digit > 5:
    print("{} {} and is greater than 5".format(prefix, last_digit))
elif last_digit == 0:
    print("{} {} and is 0".format(prefix, last_digit))
else:
    print("{} {} and is less than 6 and not 0".format(prefix, last_digit))
