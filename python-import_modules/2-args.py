#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1  # Subtract 1 to exclude the script name
    
    # Print the number of arguments
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print(f"{num_args} arguments:")
    
    # Loop through and print each argument along with its position
    for i in range(1, num_args + 1):
        print(f"{i}: {sys.argv[i]}")

