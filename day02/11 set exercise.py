attendee_names = set()
attendee_count = int(input("How many attendees? "))

for attendee in range (attendee_count):
    attendee = input("Input attendee name: ")
    attendee_names.add(attendee)

print(f"Attendee name/s: {attendee_names}")

print(f"Raffle winner: {attendee_names.pop()}")