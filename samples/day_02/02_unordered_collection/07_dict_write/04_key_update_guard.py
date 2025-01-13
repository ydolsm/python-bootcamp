student_records = {"Juan": 70, "Maria": 98, "Joseph": 81, "Elise": 80}

if "Joseph" in student_records.keys():
	print("Joseph is already recorded!")
else:
	student_records["Joseph"] = 100

print(student_records["Joseph"])