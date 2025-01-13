class Example:
    def public_method(self):
        print(1)

class Other(Example):
    def inner(self):
        self.public_method()

other = Other()
other.inner()
other.public_method()