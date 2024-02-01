# Classes and Objects
class Person:
    def __init__(self, name, age): 
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, I am {self.age}")

# Example of input from the terminal
person1 = Person(input(), int(input()))
person2 = Person(input(), int(input()))

person1.introduce()
person2.introduce()

