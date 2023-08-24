
class Class():
    def __init__(self, x):
        print(x)
class SubClass(Class):
    def __init__(self, x):
        # this is how we call super
        # class's constructor
        super().__init__(x)

# driver code
x = [1, 2, 3, 4, 5]
a = SubClass(x)



class Brand:
    def __int__(self,brand):
        self.brand = brand
    def get_brand(self):
        print("brand",self.brand)

class Products(Brand):
    def __init__(self,product_deatils):
        print(product_deatils)
        self.brand = product_deatils.get('brand')
        self.product = product_deatils.get('product')
        # super().__init__(brand)
        # self.product =product
    def get_product(self):
        print("prodct",self.product)

product_obj =Products({"brand": "Mi","product":"Redmi Note 12"})
product_obj.get_product()
product_obj.get_brand()