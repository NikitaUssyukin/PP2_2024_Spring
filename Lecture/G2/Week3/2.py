# Classes and Objects
class Person:
    name = "Linus"

    def introduce(self):
        print(f"My name is {self.name}")

person = Person()
print(person.name)

person.name = "Amina"
print(person.name)
person.introduce()


