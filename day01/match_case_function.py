color_input = input("Please enter a color: ")

match color_input:
    case "green":
        print ("Go!")
    case "yellow":
        print ("Wait...")
    case "red":
        print ("Stop!")