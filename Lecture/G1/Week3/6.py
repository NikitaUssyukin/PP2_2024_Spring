# Inheritance

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return self.name + " " + self.surname

class Student(Person):
    pass

student = Student("Linus", "Torvalds")

print(student.name)
print(student.surname)
print(student)
