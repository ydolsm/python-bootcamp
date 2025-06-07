heroes = ["Knight", "Archer", "Mage", "Cleric"]
monsters = ["Slime", "Orc", "Chocobo", "Dragon"]
pacifist = ["Cleric", "Chocobo"]

# Make a list of tuples pairing each hero with each monster
#pairing = [...]
pairing = [
    (hero, monster)
    for hero in heroes
    for monster in monsters
]

print (pairing)

def winner (hero, monster):

def condition (pairing):



#example_list = [number for number in range(11) if number % 2 == 0]

# Then, make a list of strings wherein the string with the longest length remains.
# If it’s a draw, set the value to 'Draw' instead.
# Additionally, if one of them is a pacifist, don’t include in the list.
#winners = [...]

#print(winners)