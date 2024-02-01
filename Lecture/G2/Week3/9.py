# Inheritance
class Person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created!")

    def __str__(self):
        return f"My name is {self.name}"
        

class Student(Person):
    # extending functionality
    def __init__(self, name, ID, age):
        super().__init__(name)
        self.ID = ID
        self.age = age

    # overriding
    def __str__(self):
        return f"My name is {self.name} and my ID is {self.ID}"

    # adding new method
    def attendLecture(self, date):
        print(f"{self.name} attended a lecture on {date}")
 
student1 = Student("Efim", "23B2023", "")
print(student1)

student1.attendLecture("01-02-2024")

