
import sys
class A:
    version = 0.1
    def __init__(self):
        print("default constructor")
        # self.no = no
    def feature1(self):
        print("Feature1")
    def feature2(self):
        print("Feature2")

class B(A):
    def feature3(self):
        print("Feature3")
    def feature4(self):
        print("Feature4")


obj = B()
print(id(obj))

obj.feature4()
obj.feature1()

version = 0.1

print(version)
print(id(version))

print(obj.version)
print(id(obj.version))
print()