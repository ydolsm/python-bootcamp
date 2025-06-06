number = int(input("Provide a number: "))

match number:
    case 0 | 1 | 5 | 10:
        print("Special number detected!")
    case _:
        print("Not a special number!")