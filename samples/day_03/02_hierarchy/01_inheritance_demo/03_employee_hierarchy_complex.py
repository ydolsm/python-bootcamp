class Employee:
    def __init__(self, id):
        self.id = id

    def time_in(self):
        print('Time In')

    def time_out(self):
        print('Time Out')

class Recruiter(Employee):
    def recruit(self):
        print('Recruiting')

class Developer(Employee):
    def code(self):
        print('Coding')

class Engineer(Developer):
    def review(self, code):
        print(f'Reviewed {code}')

class Designer(Employee):
    def design(self):
        print('Designing')

class Manager(Employee):
    def manage(self):
        print('Managing')

class ProductManager(Engineer, Manager):
    def open(self, ticket):
        print(f'Raised {ticket}')