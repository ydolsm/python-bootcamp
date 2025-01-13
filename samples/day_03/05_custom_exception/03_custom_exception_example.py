class InvalidChoice(Exception):
    def __init__(self, message):
        super().__init__(message)

print("Select on of the choices (number):")
print("\t1. Choice A")
print("\t2. Choice B")
print("\t3. Choice C")

user_input = input("> ")

if user_input not in ('1', '2', '3'):
    raise InvalidChoice("You can only pick 1, 2, or 3")
