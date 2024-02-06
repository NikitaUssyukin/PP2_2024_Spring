# Inheritance

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return self.name + " " + self.surname

class Student(Person):
    def __init__(self, name, surname, ID):
        self.name = name
        self.surname = surname
        self.ID = ID

    def __str__(self):
        return self.name + " " + self.surname + " " + self.ID

student = Student("Linus", "Torvalds", "23B2024")

print(student.name)
print(student.surname)
print(student.ID)
print(student)
