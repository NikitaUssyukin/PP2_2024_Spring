# Inheritance
import random

class Person:
    def __init__(self, name, age): 
        self.name = name
        self.age = age

    def __str__(self):
        return f"My name is {self.name}, I am {self.age}"

class Student(Person):
    def __init__(self, name, age, ID, university): 
        super().__init__(name, age)
        self.ID = ID
        self.university = university

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

student1 = Student("Linus", 18, "23B2023", "KBTU")
student2 = Student("Sasha", 19, "23B2024", "Oxford")

for i in range (0, 7):
    student1.passFinal("PP1")

for i in range (0, 7):
    student2.passFinal("PP2")