def menu(command):
    match command:
        case "add" | "create" | "new":
            print("Adding new song...")
        case "remove" | "delete":
            print("Removing given song...")
        case "play" | "start":
            print("Playing the first song...")
        case "show":
            print("Showing all songs...")
        case _:
            print("Unknown command...")


user_command = input("Enter command: ")
menu(user_command)
