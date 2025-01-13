class Duck:
    def __init__(self, beak):
        self.beak = beak

    def swim(self):
        print("Swimming")

    def quack(self):
        print("Quack")

class DuckPerson:
    def __init__(self, beak):
        self.beak = beak

    def swim(self):
        print("I’m a swimming duck!")

    def quack(self):
        print("Quack quack hehehe")

class RubberDuck:
    def __init__(self, beak):
        self.beak = beak

    def swim(self):
        print("Splish Splosh")

    def quack(self):
        print("Squeak Quack")

class RoastedDuck:
    def __init__(self, serving):
        self.serving = serving

ducks = []
for duck in range(10):
    ducks.append(Duck("short"))
    ducks.append(RubberDuck("squeaky"))
    ducks.append(DuckPerson("plastic"))
    ducks.append(RoastedDuck(3))

for duck in ducks:
    if hasattr(duck, 'beak') and hasattr(duck, 'quack'):
        duck.quack()
    else:
        print('Not an actual duck')