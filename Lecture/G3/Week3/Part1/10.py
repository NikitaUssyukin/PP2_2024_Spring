# Inheritance
import random

class Person:
    def __init__(self, name, age): 
        self.name = name
        self.age = age

    def __str__(self):
        return f"My name is {self.name}, I am {self.age}"

class Student(Person):
    def __init__(self, name, age, ID, university, disciplines): 
        super().__init__(name, age)
        self.ID = ID
        self.university = university
        self.disciplines = disciplines

    def __str__(self):
        return f"My name is {self.name}, I am {self.age}, My ID is {self.ID}.\n I study at {self.university}!"
    
    def passFinal(self, discipline):
        grade = random.randint(0, 40)
        if grade >= 20:
            print(f"{self.name} has passed the {discipline} exam!")
        elif grade >= 10:
            print(f"{self.name} has failed the {discipline} exam... But can try again!")
        else:
            print(f"{self.name} has failed the {discipline} exam...")

disciplines = ["PP1", "PP2", "Calculus", "English", "Discrete Math", "Physical Education"]
student1 = Student("Linus", 18, "23B2023", "KBTU", disciplines)
student2 = Student("Sasha", 19, "23B2024", "Oxford", disciplines)

for i in range(0, 7):
    index = random.randint(0, 5)
    student1.passFinal(student1.disciplines[index])

for i in range(0, 7):
    index = random.randint(0, 5)
    student2.passFinal(student2.disciplines[index])