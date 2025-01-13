from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print("Current Date and Time:")
print(now)
print()

# Formatting dates
print("Formatted Date and Time:")
print(now.strftime("%Y %B %d %H:%M:%S"))
print()

# Date arithmetic
print("Date Arithmetic:")
next_week = now + timedelta(weeks=1)
print(f"One week from now: {next_week}")
three_days_ago = now - timedelta(days=3)
print(f"Three days ago: {three_days_ago}")
print()

# Parsing a string into a datetime object
date_string = "2024-11-16 15:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed Date:")
print(parsed_date)
