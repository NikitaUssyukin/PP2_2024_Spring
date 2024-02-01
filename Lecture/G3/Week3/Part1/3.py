# Classes and Objects
class Person:
    def __init__(self, name, age): 
        print("New person created!")
        self.name = name
        self.age = age

person1 = Person("Linus", 18)
person2 = Person("Sasha", 19)

print(person1.name)
print(person1.age)

print(person2.name)
print(person2.age)