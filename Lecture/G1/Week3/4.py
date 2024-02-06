# Classes and Objects

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return self.name + " " + self.surname
    
    def greet(): 
        print("Hello all!")

person = Person("Linus", "Torvalds")

print(person.name)
print(person.surname)
print(person)

Person.greet() # won't work with person.greet()