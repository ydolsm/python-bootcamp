class Employee:
    """Class representation for employee data"""

    def __init__(self, name, id, role):
        self.name = name
        self.id = id
        self.role = role
        self.tasks = []

        print(f"Employee {name} assigned ID {id}")

    def add_work(self, task):
        return self.tasks.append(task)

employee1 = Employee("Richard","1234", "CEO")
employee2 = Employee("Jelly","9876", "COO")

print(f"Employee 1 Name: {employee1.name}, {employee1.role}")
print(f"Employee 2 Name: {employee2.name}, {employee2.role}")

employee1.add_work("review financial reports")
print(employee1.tasks)
