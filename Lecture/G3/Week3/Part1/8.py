# Inheritance
class Person:
    def __init__(self, name, age): 
        self.name = name
        self.age = age

    def __str__(self):
        return f"My name is {self.name}, I am {self.age}"

class Student(Person):
    def __init__(self, name, age, ID): 
        super().__init__(name, age)
        self.ID = ID

    def __str__(self):
        return f"My name is {self.name}, I am {self.age}, My ID is {self.ID}"

student1 = Student("Linus", 18, "23B2023")
student2 = Student("Sasha", 19, "23B2024")

print(student1)
print(student2)