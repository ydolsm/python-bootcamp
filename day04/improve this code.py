"""
def m(n):
    p = []
    for q in n:
        if q not in p:
            p.append(q)
    return p
r = [1, 2, 3, 3, 4, 5, 5]
s = m(r)
print(s)
"""

def remove_duplicate(numbers):

    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
             unique_numbers.append(number)
    return unique_numbers

number_list = [1, 2, 3, 3, 4, 5, 5]
result = remove_duplicate(number_list)
print(result)

