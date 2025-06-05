def squared(x):
    return x**2


numbers = [1, 2, 3, 4, 5]
numbers_squared = map(squared, numbers)
print(list(numbers_squared))
