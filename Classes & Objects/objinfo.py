class student:
    def __init__(self,name,age):
        self.name = name
        self.age =age
    def print_data(self):
        print(self.name,self.age)
    def __repr__(self): 
        return "Student Info Name:% s Age:% s" % (self.name, self.age) 

stud1 = student("sukrut",28)
print(stud1)
