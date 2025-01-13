counter = 0

user_input = input("Continue? ")
while user_input == "y":
    counter += 1
    user_input = input("Continue? ")

print(counter)