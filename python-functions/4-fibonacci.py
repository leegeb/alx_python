#!/usr/bin/python3
def fibonacci_sequence(n):
    fibonacci_numbers = []
    if n <= 0:
        return fibonacci_numbers
    elif n == 1:
        fibonacci_numbers append(0)
        return fibonacci_numbers
    a, b = 0, 1
    fibonacci_numbers.append(a)
    fibonacci_numbers.append(b)
    for _ in range(2, n):
        next_number = a + b
        fibonacci_numbers.append(next_number)
        a, b = b, next_number
        return fibonacci_numbers
        
