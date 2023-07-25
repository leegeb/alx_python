#!/usr/bin/python3
def raise_exception():
    x = "Hello"
    y = 5
    if not isinstance(x, int):
        raise TypeError("x must be an integer.")
    elif not isinstance(y, str):
        raise TypeError("y must be a string.")

