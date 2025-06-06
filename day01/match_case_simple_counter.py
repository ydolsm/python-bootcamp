count = 0
stop_program = False
while not stop_program:
    choice = input ("Provide command: ")
    match count:
        case "add":
           count += 1
           print (count)
        case "minus":
            count -= 1
            print (count)
        case "exit":
            stop_program = True