class A:
    def method(self):
        print("A method is called")

class B:
    def method(self):
           print("B method is called")

class C(A,B):
       pass

class D(C,B):
    pass
d = D()
d.method()