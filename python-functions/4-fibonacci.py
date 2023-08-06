#!/usr/bin/python3
def fibonacci_sequence(n):
    sequence=[0, 1]
    if n <= 1:
        return  sequence[:n]
    else:
        while len(sequence) < n:
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)
        return sequence
