class Parent:
    def sing(self):
        print("Singing: When I met You")

class Child(Parent):
    def sing(self):
        super().sing()
        print(f"Singing: Let it Go")

parent = Parent()
parent.sing()

child = Child()
child.sing()