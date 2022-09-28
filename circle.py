
import math

class Circle():
    def __init__(self, radius=0, diameter=0, circumference=0):
        self.radius = radius
        self.diameter = diameter
        self.circumference = circumference

    def calculate_circle_details(self):
        print("------------",self.radius,self.diameter,self.circumference)

        if self.radius != 0:
            self.diameter = self.radius * self.radius
            self.area = math.pi * self.radius * self.radius
            self.circumference = (2 * math.pi) * self.radius
            return 0

        if self.diameter != 0:
            self.radius = self.diameter / 2
            self.area = math.pi * self.radius * self.radius
            self.circumference = (2 * math.pi) * self.radius
            return 0

        if self.circumference != 0:
            self.radius = self.circumference /(2 * math.pi)
            self.diameter = 2 * self.radius
            self.area = math.pi * self.radius * self.radius
            return 0

    def get_circle_details(self):
        self.calculate_circle_details()
        print("---------------------------")
        print("---circle radius = ",self.radius)
        print("---circle diameter = ", self.diameter)
        print("---circle circumference = ", self.circumference)
        print("---circle area = ", self.area)


print("Please Enter choice for circle Details")
print("1.Enter radius")
print("2.Enter Diameter")
print("3.circumference")

choice = int(input("Enter your choice"))
radius,diameter,circumference =0, 0, 0

if choice in [1,2,3]:
    if choice == 1:
        radius = float(input("Enter radius"))
        print(Circle(radius,diameter,circumference).get_circle_details())
    elif choice ==2:
        diameter = float(input("Enter Diameter"))
        print(Circle(radius,diameter,circumference).get_circle_details())
    elif choice ==3:
        circumference = float(input("Enter circumference"))
        print(Circle(radius,diameter,circumference).get_circle_details())
else:
    print("wrong Choice")

