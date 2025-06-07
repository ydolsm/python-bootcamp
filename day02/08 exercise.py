#Allowed list exercise
names = ["Alfonso", "Joaquin", "Carlos"]

user_name = input("Please provide your name: ")

if user_name in names:
    print("Access granted!")
else:
    print ("Access denied!")