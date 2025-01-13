class Parent:
    def __init__(self, likes):
        self.likes = likes

    def sing(self):
        print("Singing")

class Child(Parent):
    def __init__(self, likes, toy):
        super().__init__(likes)
        self.toy = toy

    def play(self):
        print(f"Playing {self.toy}")

child = Child("Milk", "Lego")
child.sing()


