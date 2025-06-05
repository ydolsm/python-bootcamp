import re


def is_valid_email(email):
    # Define the regex pattern for a valid email
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # Use re.match to check if the email matches the pattern
    return re.match(pattern, email) is not None


# Test the function
emails = [
    "example@example.com",
    "user.name@domain.co",
    "user-name@sub.domain.com",
    "invalid-email@domain",
    "another.invalid@.com",
    "@missingusername.com",
    ".@..com",
]

for email in emails:
    if is_valid_email(email):
        status = "Valid"
    else:
        status = "Invalid"

    print(f"{email}: {status}")
