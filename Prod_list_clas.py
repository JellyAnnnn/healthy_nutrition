import json

class Product:
    def __init__ (self, name, protein, fat, carb):
        self.name = name
        self.protein = protein
        self.fat = fat
        self.carb = carb

class ProductService:
    def request_func (self, name, amount):
        products = {
            "apple": Product(name='Apple', protein=0.44, fat=0.19, carb=10.81),
            "grapefruit": Product(name='Grapefruit', protein=0.7, fat=0.2, carb=6.5),
            "bananа": Product(name='Bananа', protein=1.5, fat=0.5, carb=21),
            "orange": Product(name='Orange', protein=0.9, fat=0.2, carb=8.1)
        }
        # name = "apple"
        # amount = 5

        if name not in products:
            print('key not found')
        else:
            return Calc_cal(products[name], amount)

class ProductItem:
    def __init__ (self, prod_protein, prod_fat, prod_carb):
        self.prod_protein = prod_protein
        self.prod_fat = prod_fat
        self.prod_carb = prod_carb

    def toJSON (self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

def Calc_cal (product, amount):
    my_cal_result_obj = ProductItem(
        prod_protein=product.protein * amount * 4,
        prod_fat=product.fat * amount * 9,
        prod_carb=product.carb * amount * 4
    )
    return my_cal_result_obj

def Calc_grams (self, amount):
    return [self.name], [self.protein * amount], [self.fat * amount], [self.carb * amount]

# apple_product = Product(name='Apple', protein=0.44, fat=0.19, carb=10.81)
# grapefruit_product = Product(name='Grapefruit', protein=0.7, fat=0.2, carb=6.5)
# banan_product = Product(name='Banana', protein=1.5, fat=0.5, carb=21)
# orange_product = Product(name='Orange', protein= 0.9, fat= 0.2, carb= 8.1)
#
# print(apple_product.name)
# print(Calc_cal(apple_product, 5))
# print(Calc_grams(apple_product,5))

# print(apple_product.__class__)
