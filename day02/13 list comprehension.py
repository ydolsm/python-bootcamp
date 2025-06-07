#long cut
numbers = []

for number in range(11):
    numbers.append(number + 1)
print(numbers)

#simplified/shortcut syntax
#append part removed
numbers = [number + 1 for number in range(11)]
print(numbers)

#with condition
numbers = [number for number in range(11) if number % 2 == 0]
print(numbers)