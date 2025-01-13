class Example:
    def _protected_method(self):
        print(2)

class Other(Example):
    def inner(self):
        self._protected_method()

other = Other()
other.inner()
other._protected_method()