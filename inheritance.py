import sys
class Base:
    def __init__(self):
        self.member ="Sukrut"
        self._protected ="ABC"
        self.__private ="jjjj"
        print("base class default constructor")
    def get_member(self):
        print(self.member)

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Derived class default constructor")
        print(self._protected)
        print(self.__private)
d = Derived()
print(d.member)
print(d._protected)
# print(d.__private)
d.get_member()
d_size = sys.getsizeof(d)
print(d_size)



