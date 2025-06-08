class Duck:
    def __init__(self, beak):
        self.beak = beak
    def swim(self):
        print("Swimming")
    def quack(self):
        print("Quack")

class RubberDuck:
    def __init__(self, beak):
        self.beak = beak
    def swim(self):
        print("Splish Splosh")
    def quack(self):
        print("Squeak Quack")

class DuckPerson:
    def __init__(self, beak):
        self.beak = beak
    def swim(self):
        print("Swim hehe!")
    def quack(self):
        print("Quack hehe")

class RoastedDuck:
    def __init__(self, serving):
        self.serving = serving

ducks = [
    Duck("yellow"),
    RubberDuck("plastic"),
    DuckPerson("leather")
]

for duck in ducks:
    duck.quack()
    duck.swim()

dish = RoastedDuck(1)
if hasattr(dish, 'beak') and hasattr(dish, 'quack'):
    dish.quack()
else:
    print("Dinner is served")