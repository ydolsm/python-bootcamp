message = input("Enter your message: ")


lower_count = 0
upper_count = 0
space_count = 0

for every_char in message:
    if every_char.islower():
        lower_count += 1
    elif every_char.isupper():
        upper_count += 1
    elif every_char.isspace():
        space_count += 1

print("Lower case count: ", lower_count)
print("Upper case count: ", upper_count)
print("Space count: ", space_count)