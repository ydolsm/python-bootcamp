# Keep asking for user choicer
# If user says "add", increase count by 1
# Else, if user says "minus", decrease count by 1
# Else, if user says "exit", print count and end code

count = 0
stop_program = False

while not stop_program:
    choice = input("Provide command: ")
    if choice == "command 1":
        print()
    elif choice == "exit":
        stop_program = True