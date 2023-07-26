#!/usr/bin/python3
def fibonacci_sequence(n):
    if n <= 0:
        return []

    sequence = [0, 1] 
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2] 
        sequence.append(next_num)

    return sequence