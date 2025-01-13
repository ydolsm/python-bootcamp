class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []

        print(f"Employee {name} assigned ID {id}")

    def work(self, task):
        return self.tasks.append(task)

employee = Employee("Richard", "1234")
employee.work("create charts")
print(employee.tasks)