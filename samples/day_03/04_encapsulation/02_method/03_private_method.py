class Example:
    def __private_method(self):
        print(3)

class Other(Example):
    def inner(self):
        self.__private_method()

other = Other()
other.inner()
other.__private_method()