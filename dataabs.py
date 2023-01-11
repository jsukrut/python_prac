class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
        print("Base Class Initialized")

# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        # Base.__init__(self)
        # print("Calling private member of base class: ")
        #print(self.__c)
        print("Derived Class Initalized")


# Driver code
#obj1 = Base()
#print(obj1.a)

obj1 = Derived()
print(help(obj1))
