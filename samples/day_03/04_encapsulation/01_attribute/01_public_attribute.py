class Example:
    def __init__(self):
        self.public = 1

class Other(Example):
    def __init__(self):
        super().__init__()
        print(self.public)

other = Other()