class Parent:
	pass

class Child(Parent):
	pass

child = Child()
print(isinstance(child, Parent))