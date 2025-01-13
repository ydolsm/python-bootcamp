class Example:
    def __init__(self):
        self.__private = 3

class Other(Example):
    def __init__(self):
        super().__init__()
        print(self.__private)

other = Other()