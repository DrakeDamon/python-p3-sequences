#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = [0, 1]  # Start with the first two numbers
    for i in range(2, length):
        next_value = fibonacci[-1] + fibonacci[-2]  # Sum of the last two numbers
        fibonacci.append(next_value)
    print(fibonacci[:length])  # Print up to the specified length

print_fibonacci(9)
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21]
