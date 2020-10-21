'''Build two classes of your choice that can model a real-life example. The class needs to meet the following requirements:
    at least 5 attributes each
    at least 2 methods each
    one class to inherit from another
As a demonstration create at least 5 instances of one class (preferably the child class) and call all the methods it holds'''


class SupermarketProduct(object):

    def __init__(self, product_brand, product_type, product_origin, product_price, product_quantity):
        self.product_brand = product_brand
        self.product_type = product_type
        self.product_origin = product_origin
        self.product_price = product_price
        self.product_quantity = product_quantity

    def sell_product(self, items_to_sell):
        if self.product_quantity >= items_to_sell:
            self.product_quantity -= items_to_sell
            return f'We sold {items_to_sell} of the product {self.product_type}. Remaining units of this product are {self.product_quantity}'
        else:
            return f'Stock insufficient to proceed with sale of {items_to_sell} {self.product_type}. Please restock or change number of items you want to sell.'

    def restock_product(self, number_to_restock):
        self.product_quantity += number_to_restock
        return f'{self.product_type} brand {self.product_brand} has been restocked with {number_to_restock} units, ' \
               f'and the total inventory is now {self.product_quantity}'

    def __repr__(self):
        product_name = type(self).__name__
        return f'{product_name}, ID {id(self)}: {self.product_brand} - {self.product_type} - {self.product_origin} ' \
               f'- {self.product_quantity}'

    def __str__(self):
        return 'You are looking at the product {} brand {} from {} with the ' \
               'price {} euros'.format(self.product_type, self.product_brand, self.product_origin, self.product_price)

product_test = SupermarketProduct('Nivea', 'Deodorant', 'Germany', 3, 20)

print(product_test.sell_product(10))
print(product_test.sell_product(50))
print(product_test.restock_product(40))
print(repr(product_test))
print(str(product_test))


class FoodProduct(SupermarketProduct):

    def __init__(self, product_brand, product_type, product_origin, product_price, product_quantity, days_to_expiry, contains_allergens):
        self.days_to_expiry = days_to_expiry
        self.contains_allergens = contains_allergens
        super().__init__(product_brand, product_type, product_origin, product_price, product_quantity)

    # def check_expiry_date(self, days_to_check):
    #
