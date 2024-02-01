# Inheritance
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person with name {self.name} created!")

    def __str__(self):
        return f"My name is {self.name}"
        

class Student(Person):
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def __str__(self):
        return f"My name is {self.name} and my ID is {self.ID}"

    
 
student1 = Student("Efim", "23B2023")
print(student1)

