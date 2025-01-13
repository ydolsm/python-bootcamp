def round_to_n_decimals(number, n):
    return round(number, n)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
