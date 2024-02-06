# Inheritance

class University():
    def __init__(self, name, faculties):
        self.name = name
        self.faculties = faculties

class Faculty():
    def __init__(self, name, courses):
        self.courses = courses
        self.name = name

SITE = Faculty("SITE", ["PP1", "PP2", "Discrete Math", "Databases"])
BS = Faculty("BS", ["Startups", "Stocks"])
ISE = Faculty("ISE", ["Finance", "Microeconomics", "Macroeconomics"])

KBTU = University("KBTU", {"SITE": SITE, "BS": BS, "ISE": ISE})

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return self.name + " " + self.surname

class Student(Person):
    def __init__(self, name, surname, ID, university, faculty):
        super().__init__(name, surname)
        self.ID = ID
        self.university = university
        self.faculty = self.university.faculties[faculty]
        self.courses = self.faculty.courses

    def __str__(self):
        return super().__str__() + f" from {self.university.name}, {self.faculty.name} with ID {self.ID}"
   
student = Student("Linus", "Torvalds", "23B2024", KBTU, "SITE")

print(student.name)
print(student.surname)
print(student.ID)
print(student)
