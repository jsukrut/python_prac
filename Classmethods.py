class Person:
    age_for_adult = 18
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender =gender

    def info(self):
        print(f"executing foo({self})")
        print(f"Name = ({self.name})")
        print(f"Age = ({self.age})")
        print(f"Gender = ({self.gender})")
        print(self.age_for_adult)
    @classmethod
    def create_person(cls,name,age,gender):
        print("class")
        print(cls.is_adult(int(age)))
        print(cls.age_for_adult)
        return Person(name,age,gender)
    @staticmethod
    def is_adult(age):
        return True if age > 18 else False
person1 = Person("Sukrut",29,"Male")
person1.info()
Person.is_adult(person1.age)
person1.is_adult(person1.age)
person2= person1.create_person("Mohini",29,"Female")
print(person2)
person2.info()
person2.age_for_adult =20
print(person2.age_for_adult)
print(person1.age_for_adult)
Person.age_for_adult =21
print(person2.age_for_adult)
print(person1.age_for_adult)
person2 = Person.create_person("Mona","29","Female")
