name_message = "Your name is {}."
number_message = "Your favorite number is {}."
color_message = "Your favorite color is {}."

user_name = input("Your name: ")
favorite_number = input("Your favorite number: ")
favorite_color = input ("Your favorite color: ")

formatted_name_message = name_message.format (user_name)
formatted_favorite_number = favorite_number.format (favorite_number)
formatted_favorite_color = favorite_color.format (favorite_color)