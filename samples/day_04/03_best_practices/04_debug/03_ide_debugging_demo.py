def factorial(n):
    if n < 0:
        return "Invalid input: factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 2):
            result *= i
        return result

def main():
    num = int(input("Enter a non-negative integer: "))
    fact = factorial(num)
    print(f"The factorial of {num} is {fact}")

if __name__ == "__main__":
    main()
