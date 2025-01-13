attendee_names = []

attendee_count = int(input("How many attendees? "))

for attendee in range(attendee_count):
    attendee_name = input("attendee name: ")
    attendee_names.append(attendee_name)

print(attendee_names)

my_name = "Joseph"
print(f"Same Name: {attendee_names.count(my_name)}")

# Remove the last attendee name
late_attendee = attendee_names.pop(-1)
print(f"Late Attendee: {late_attendee}")

for number, name in enumerate(attendee_names, start=1):
    print(f"Attendee {number}: {name}")

# From the previous exercise, print again the names in attendee_names,
# but this time in alphabetical order (the removed attendee should still be removed).