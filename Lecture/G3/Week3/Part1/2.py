# Classes and Objects
class Person:
    name = "Linus"
    age = 18

person1 = Person()
person2 = Person()

print(person2.name)
print(person2.age)

print("===")

person2.name = "Sasha"
person2.age = 19

print(person1.name)
print(person1.age)

print(person2.name)
print(person2.age)