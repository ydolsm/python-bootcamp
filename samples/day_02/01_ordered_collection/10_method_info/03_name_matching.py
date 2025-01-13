attendee_names = []

attendee_count = int(input("How many attendees? "))

# Based on the attendee_count, ask the user for that many attendee names
for attendee in range(attendee_count):
    attendee_name = input("attendee name: ")
    attendee_names.append(attendee_name)

print(attendee_names)

# Print the number of attendees with the same name as you.
#   Example:
#       Same Name: 3
