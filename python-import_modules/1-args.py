#!/usr/bin/python3
import sys
from typing import List

def main(argv: List[str]) -> None:
    args = argv[1:]  
    num_args = len(args)

    print(f"Number of argument(s): {num_args}", end="")
    print(" argument" if num_args == 1 else " arguments", end="")
    print(f":{'.' if num_args == 0 else ''}")

    for i, arg in enumerate(args, 1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    main(sys.argv) 
