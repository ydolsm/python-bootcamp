def factorial(n):
    if n < 0:
        print(f"Invalid input: factorial is not defined for negative numbers.")
        return None
    elif n == 0:
        print(f"The factorial of 0 is 1.")
        return 1
    else:
        result = 1
        print(f"Calculating factorial for {n}:")
        for i in range(1, n + 2):
            result *= i
            print(f"Multiplying {result} by {i} gives {result}")
        print(f"The factorial of {n} is {result}.")
        return result

def main():
    num = int(input("Enter a non-negative integer: "))
    fact = factorial(num)
    print(f"The factorial of {num} is {fact}.")

if __name__ == "__main__":
    main()
