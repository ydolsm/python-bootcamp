count = 0
stop_program = False
while not stop_program:
    choice = input ("Provide command: ")
    if choice == "add":
        count += 1
        print (count)
    elif choice == "minus":
        count -= 1
        print (count)
    elif choice == "exit":
        stop_program = True
