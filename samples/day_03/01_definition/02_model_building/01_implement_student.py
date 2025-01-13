class Student:

    def __init__(self, name, group):
        self.name = name
        self.group = group

    def introduce(self):
        print(f"My name is {self.name} from group {self.group}")

student1 = Student("Juan", 'a')
student1.introduce()

student2 = Student("Maria", 'b')
student2.introduce()