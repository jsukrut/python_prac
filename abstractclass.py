
class ABC:

    def method1(self):
        print("base class")
        pass

    def method2(self):
        pass

class A(ABC):
    def __init__(self,a):
        self.a = a
    def method1(self):
        super().method1()
        print("Implement in child class")
        print(self.a)


obj =A(10)
obj.method1()