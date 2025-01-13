from functools import lru_cache, partial

# Example of lru_cache
@lru_cache(maxsize=3)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print("Fibonacci Sequence:")
for i in range(10):
    print(f"fib({i}) = {fib(i)}")
print()

# Example of partial
def multiply(x, y):
    return x * y

double = partial(multiply, y=2)
print("Using Partial:")
print(f"Double of 5 is {double(5)}")
