def mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def variance(numbers):
    if len(numbers) < 2:
        return 0
    avg = mean(numbers)
    return sum((x - avg) ** 2 for x in numbers) / (len(numbers) - 1)

def standard_deviation(numbers):
    return variance(numbers) ** 0.5
