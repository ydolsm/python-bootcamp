"""
pdb: Python Debugger

    n (next): Execute the next line of code.
    c (continue): Continue execution until the next breakpoint.
    p variable_name: Print the value of variable_name.
    q (quit): Exit the debugger.

"""

import pdb

def factorial(n):
    pdb.set_trace()  # Set a breakpoint to inspect the input value
    if n < 0:
        return "Invalid input: factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
            pdb.set_trace()  # Set a breakpoint to inspect 'result' and 'i' during each iteration
        return result

def main():
    num = int(input("Enter a non-negative integer: "))
    fact = factorial(num)
    print(f"The factorial of {num} is {fact}")

if __name__ == "__main__":
    main()
