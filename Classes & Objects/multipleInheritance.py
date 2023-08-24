class Brand:
    def __int__(self,brand):
        self.brand = brand
    def get_brand(self):
        print("brand",self.brand)

class Products():
    def __init__(self,product):
        self.product = product
    def get_product(self):
        print("product",self.product)


class Popularity(Brand,Products):
    def __init__(self,product_details):
        print("-------")
        self.brand =product_details.get('brand')
        self.product =product_details.get('product')
        self.popularity = product_details.get('popularity')
    def get_popularity(self):
        print("popularity",self.popularity)

product_details ={
    "brand": "Redmi",
    "product":"MI Note 12",
    "popularity":"70"
}
product_obj = Popularity(product_details)
product_obj.get_product()
product_obj.get_brand()
product_obj.get_popularity()