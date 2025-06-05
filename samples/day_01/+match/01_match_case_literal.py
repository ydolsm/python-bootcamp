you_said = input("You said: ")

match you_said:
    case "Wish":
        print("107.5")
    case "Hello":
        print("...it’s me")
    case "Jopay":
        print("...kamusta ka na")
    case "Black Pink":
        print("...in your area")
    case _:
        print("I don’t know that song!")
