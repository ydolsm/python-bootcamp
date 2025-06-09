def average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
numbers = [10, 20, 30, 40]
print(average(numbers))

