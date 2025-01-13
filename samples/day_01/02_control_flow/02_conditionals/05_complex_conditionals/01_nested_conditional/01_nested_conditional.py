age = int(input("Enter age: "))
is_member = input("Member? (y/n) ")

if age > 18:
	if is_member == "y":
		print("Welcome! You get discount")
	else:
		print("Welcome!")
else:
	print("Not allowed!")