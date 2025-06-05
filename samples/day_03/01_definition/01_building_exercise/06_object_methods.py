class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []

        print(f"Employee {self.name} assigned ID {self.id}")

    def work(self, task):
        return self.tasks.append(task)


employee = Employee("Richard", "1234")
employee2 = Employee("Jelly", "9876")

employee.work("create charts")
print(employee.tasks)
