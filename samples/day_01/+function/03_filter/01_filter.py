def is_even(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5]
numbers_even = filter(is_even, numbers)
print(list(numbers_even))
