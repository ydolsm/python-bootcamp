class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id

        print(f"Employee {self.name} assigned ID {self.id}")


employee1 = Employee("Richard", "1234")
employee2 = Employee("Jelly", "9876")

print(employee1.name)
print(employee2.name)
