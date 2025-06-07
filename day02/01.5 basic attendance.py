attendee_names = []
attendee_count = int(input("How many attendees? "))

for attendee in range (attendee_count):
    attendee = input("Input attendee name: ")
    attendee_names.append(attendee)
print(f"Attendee name/s: {attendee_names}")


