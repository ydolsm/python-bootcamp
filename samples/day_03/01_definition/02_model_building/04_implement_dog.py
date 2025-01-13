class Dog:

	population = 0

	def __init__(self, name, good_boy = True):
		self.name = name
		self.good_boy = good_boy
		Dog.population = Dog.population + 1

	def bark(self):
		print("Bark")

dog = Dog("Rocky")
print(Dog.population)
