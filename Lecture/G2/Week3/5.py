# Classes and Objects
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person with name {self.name} created!")

    def introduce(self):
        print(f"My name is {self.name}")

person1 = Person("Linus")

print(person1)




