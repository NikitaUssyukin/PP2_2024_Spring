# Classes and Objects

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

person = Person("Linus", "Torvalds")

print(person.name)
print(person.surname)
print(person)