number_count = int(input("How many to generate? "))

squares = [number ** 2 for number in range(number_count)]
print(squares)

#long cut
numbers = []
number_count = int(input("How many to generate? "))

for number in range(number_count):
    numbers.append(number ** 2)
print(numbers)