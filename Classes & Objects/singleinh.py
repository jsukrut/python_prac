
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

class Employee(Person):
    def __init__(self,name,age,id):
        self.id = id
        # self.name = name
        # self.age = age
        super().__init__(name,age)
        print(super().IsAdult(age))
    def getEmployeeDetails(self):
        return(self.name,self.age,self.id)


emp = Employee("Sukrut Joshi",28,111)
print(emp.getEmployeeDetails())