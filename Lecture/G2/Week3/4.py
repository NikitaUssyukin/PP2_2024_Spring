# Classes and Objects
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person with name {self.name} created!")

    def introduce(self):
        print(f"My name is {self.name}")

person1 = Person("Linus")
person2 = Person("Amina")
person3 = Person("Nikita")

person1.introduce()



