# Classes and Objects
class Person:
    def __init__(self, name, age): 
        self.name = name
        self.age = age

    def __str__(self):
        return f"My name is {self.name}, I am {self.age}"

person1 = Person("Linus", 18)
person2 = Person("Sasha", 19)

print(person1)
print(person2)


