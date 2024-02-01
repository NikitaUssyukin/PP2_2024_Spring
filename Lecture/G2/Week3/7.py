# Inheritance
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person with name {self.name} created!")

    def __str__(self):
        return f"My name is {self.name}"
        

class Student(Person):
    pass

student1 = Student("Efim")
print(student1)

