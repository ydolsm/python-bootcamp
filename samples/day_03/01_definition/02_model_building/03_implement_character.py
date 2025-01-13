class Character:

    def __init__(self, health=10, power=0, shield=0):
        self.health = health
        self.power = power
        self.shield = shield

    def attack(self, other):
        other.health = other.health - (self.power - other.shield)


player = Character(power=100)
enemy = Character()
player.attack(enemy)
print(enemy.health)
