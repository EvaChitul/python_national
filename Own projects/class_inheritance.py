'''Build two classes of your choice that can model a real-life example. The class needs to meet the following requirements:
    at least 5 attributes each
    at least 2 methods each
    one class to inherit from another
As a demonstration create at least 5 instances of one class (preferably the child class) and call all the methods it holds'''


class SupermarketProduct(object):

    def __init__(self, product_type, product_origin, product_price, product_quantity):
        self.product_type = product_type
        self.product_origin = product_origin
        self.product_price = product_price
        self.product_quantity = product_quantity

    def sell_product(self, items_to_sell):
        if self.product_quantity >= items_to_sell:
            print('We can sell', items_to_sell, 'of the product', self.product_type)
        else:
            print(f'Stock insufficient to proceed with sale of {items_to_sell} {self.product_type}. Please restock or change number of items you want to sell.')

    def restock_product(self, number_to_restock):
        return f'{self.product_type} has been restocked with {number_to_restock} units'


product_test = SupermarketProduct('deodorant', 'germany', 3, 20)

product_test.sell_product(10)
product_test.sell_product(50)
print(product_test.restock_product(40))

