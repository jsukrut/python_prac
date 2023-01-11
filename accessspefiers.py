class Student:
    __schoolName = 'XYZ School' # private class attribute
    _schoolName = 'XYZ School'  # protected class attribute
    schoolName = 'XYZ School' # class attribute

    def __init__(self, name, age):
        self._name = name #Protected attribute
        self.__name = name  # private instance attribute
        self.__age = age # private instance attribute
    def __display(self):  # private method
	    print('This is private method.')

class Representative(Student):
    def __init__(self,class_name,name,age):
        super().__init__(name,age)
        self.class_name = class_name
    def info(self):
        print(self.class_name)
        print("inherited protected memeber")
        print(self._name)
        print(self.schoolName)
        print("inherited private memeber")
        print(self._Student__name)


std = Student("Bill", 25)

print("class attributes")
print(std.schoolName)

print("Protected attributes")
print(std._name)
std._name ="Rakesh"
print(std._name)

print("Private attributes")
print(std._Student__name)



std1 = Representative("III","Bill", 25)
std1.info()


