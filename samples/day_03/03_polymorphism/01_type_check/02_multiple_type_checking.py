class Unrelated:
	pass

class Parent:
	pass

class Child(Parent):
	pass

child = Child()
type_check = isinstance(child,(Unrelated, Parent))
print(type_check)
