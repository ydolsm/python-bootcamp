class Example:
    def __init__(self):
        self._protected = 2

class Other(Example):
    def __init__(self):
        super().__init__()
        print(self._protected)

other = Other()