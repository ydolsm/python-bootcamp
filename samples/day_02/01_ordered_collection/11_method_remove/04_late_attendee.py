attendee_names = []

attendee_count = int(input("How many attendees? "))

for attendee in range(attendee_count):
    attendee_name = input("attendee name: ")
    attendee_names.append(attendee_name)

print(attendee_names)

my_name = "Joseph"
print(f"Same Name: {attendee_names.count(my_name)}")

# Remove the last attendee name
# and print their name with the following format:
#   Late Attendee: Attendee Name