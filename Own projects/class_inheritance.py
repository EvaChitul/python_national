'''Build two classes of your choice that can model a real-life example. The class needs to meet the following requirements:
    at least 5 attributes each
    at least 2 methods each
    one class to inherit from another
As a demonstration create at least 5 instances of one class (preferably the child class) and call all the methods it holds'''


class SupermarketProduct(object):

    def __init__(self, product_brand, product_type, product_origin, product_price, product_quantity, product_unit):
        self.product_brand = product_brand
        self.product_type = product_type
        self.product_origin = product_origin
        self.product_price = product_price
        self.product_quantity = product_quantity
        self.product_unit = product_unit

    def sell_product(self, items_to_sell):
        if self.product_quantity >= items_to_sell:
            self.product_quantity -= items_to_sell
            return f'We sold {items_to_sell} {self.product_unit} of the product {self.product_type} {self.product_brand}.' \
                   f' Remaining {self.product_unit} of this product are {self.product_quantity} \n'
        else:
            return f'Stock insufficient to proceed with sale of {items_to_sell} {self.product_unit} {self.product_type} {self.product_brand}.' \
                   f' Please restock or change number of items you want to sell. \n'

    def restock_product(self, number_to_restock):
        self.product_quantity += number_to_restock
        return f'{self.product_type} brand {self.product_brand} has been restocked with {number_to_restock} {self.product_unit}, ' \
               f'and the total inventory is now {self.product_quantity} {self.product_unit}\n'

    def __repr__(self):
        product_name = type(self).__name__
        return f'Admin view: {product_name}, Type {type(self)} ID {id(self)}: {self.product_brand} - {self.product_type} ' \
               f'- {self.product_origin} - {self.product_quantity} - {self.product_unit} \n'

    def __str__(self):
        return 'Client view: You are looking at the product {} brand {} from {} with the ' \
               'price {} euros \n'.format(self.product_type, self.product_brand, self.product_origin, self.product_price )


deodorant_nivea = SupermarketProduct('Nivea', 'Deodorant', 'Germany', 3, 20, 'Pack(s)')
cleaning_product = SupermarketProduct('Dreft', 'Dish Soap', 'Netherlands', 1.5, 30, 'Piece(s)')

print(deodorant_nivea.sell_product(10))
print(deodorant_nivea.sell_product(50))
print(deodorant_nivea.restock_product(40))
print(repr(deodorant_nivea))
print(str(deodorant_nivea))
print(cleaning_product.sell_product(3))
print(cleaning_product.restock_product((21)))


class FoodProduct(SupermarketProduct):

    def __init__(self, product_brand, product_type, product_origin, product_price, product_quantity, product_unit, contains_allergens = None):
        self.contains_allergens = contains_allergens if contains_allergens else None
        super().__init__(product_brand, product_type, product_origin, product_price, product_quantity, product_unit)

    def allergens_check(self, allergies = None):
        if allergies:
            self.contains_allergens = allergies
            return f'The product {self.product_type} {self.product_brand} contains allergens.'
        else:
            return f'The product {self.product_type} {self.product_brand} does not contain any known allergens.'

    def __str__(self):
        if self.contains_allergens:
            return 'Client view: You are looking at the product {} brand {} from {} with the ' \
               'price {} euros that contains {} allergens \n'.format(self.product_type, self.product_brand,
                self.product_origin, self.product_price, self.contains_allergens)
        else:
            return 'Client view: You are looking at the product {} brand {} from {} with the ' \
                   'price {} euros that contains no allergens \n'.format(self.product_type,
                    self.product_brand, self.product_origin, self.product_price)

    @staticmethod
    def welcome_message():
        return 'Welcome to the Food Section! \n'


print(FoodProduct.welcome_message())

nutella_product = FoodProduct('Nutella', 'Sweets', 'France', 7, 10, 'Pack(s)', 'nuts')
pasta_product = FoodProduct('Barilla', 'Pasta', 'Italy', 5, 30, 'Pack(s)')
halloumi_product = FoodProduct('Galbani', 'Cheese', 'Cyprus', 4, 50, 'Pack(s)')
meat_product = FoodProduct('Farm', 'Meat / Chicken', 'Belgium', 10, 15, 'KG(s)')
bio_product = FoodProduct('Delhaize', 'Milk / Almond', 'Ireland', 2, 30, 'Litre(s)')

print(nutella_product.allergens_check('nuts'))
print(pasta_product.allergens_check())
print(nutella_product.sell_product(20))
print(halloumi_product.restock_product(10))
print(str(nutella_product))
print(str(halloumi_product))
print(meat_product.allergens_check())
print(repr(meat_product))
print(bio_product.restock_product(23))
print(meat_product.sell_product(5))
print(halloumi_product.restock_product(47))
