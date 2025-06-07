attendees = dict()
attendee_count = int(input("How many attendees? "))

for attendee in range (attendee_count):
    name = input("Input attendee name: ")
    task = input("Input attendee task: ")
    attendees[name]=task
print(attendees)

