from datetime import date

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def fromBirthYear(cls,name,year):
        return cls(name, date.today().year - year)
    @staticmethod
    def IsAdult(age):
        return age >18


person1 = Person("Sukrut",28)
person2 = Person.fromBirthYear("Sukrut",1992)
print(person1.age)
print(person2.age)


