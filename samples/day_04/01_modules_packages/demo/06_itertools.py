from itertools import permutations, combinations, cycle, islice

# Permutations
print("Permutations of [1, 2, 3]:")
for perm in permutations([1, 2, 3]):
    print(perm)
print()

# Combinations
print("Combinations of 2 from [1, 2, 3]:")
for comb in combinations([1, 2, 3], 2):
    print(comb)
print()

# Cycle
print("Cycling through ['A', 'B', 'C'] (3 iterations):")
cyclic = cycle(['A', 'B', 'C'])
print(list(islice(cyclic, 9)))  # Get 9 items from the cycle
